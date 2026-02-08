from flask import Flask, request, session, jsonify
import mysql.connector
from flask_cors import CORS
import bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from functools import wraps
import secrets
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(24))
# Enable CORS with credentials support for frontend on port 8000
CORS(app, supports_credentials=True, origins=["http://127.0.0.1:8000", "http://localhost:8000"])

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_route'  # Match the actual function name

# Simple User model for Flask-Login
class User(UserMixin):
    def __init__(self, user_id, username, role):
        self.id = user_id
        self.username = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute('SELECT user_id, username, role FROM userstb WHERE user_id=%s AND status=%s', (user_id, 'active'))
        user_data = cursor.fetchone()
        if user_data:
            return User(user_data['user_id'], user_data['username'], user_data['role'])
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass
    return None

def role_required(required_roles):
    """Decorator to enforce role-based access control."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return {"status": "fail", "message": "Not authenticated"}, 401
            if current_user.role not in required_roles:
                return {"status": "fail", "message": "Insufficient permissions"}, 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3033",
    database="student_erp_db"
)


def get_db_connection():
    """Return a new MySQL connection using the same settings as the global `db`.
    Callers should close the connection when finished.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="3033",
        database="student_erp_db"
    )

@app.route("/")
def home():
    return "ERP Backend Connected Successfully!"

# admission forms..............................................................................

@app.route("/admission", methods=["POST"])
def admission():
    db = get_db_connection()
    cursor = db.cursor()

    full_name = request.form["full_name"]
    dob = request.form["dob"]
    gender = request.form["gender"]
    department = request.form["department"]
    year = request.form["year"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    # Insert student
    cursor.execute("""
        INSERT INTO student_mastertb
        (full_name, dob, gender, department, year, email, mobile, admission_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())
    """, (full_name, dob, gender, department, year, email, mobile))

    db.commit()
    student_id = cursor.lastrowid

    # Create student login (hashed password)
    hashed_password = bcrypt.hashpw(dob.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("""
        INSERT INTO userstb (username, password, role, status)
        VALUES (%s, %s, 'student', 'active')
    """, (str(student_id), hashed_password))

    db.commit()

    cursor.close()
    db.close()

    return f"""
    <h2>Admission Successful</h2>
    <p><b>Your Student ID is: {student_id}</b></p>
    <p>Login Username: {student_id}</p>
    <p>Password: {dob}</p>
    """


# fees ...................................................................

@app.route("/fee", methods=["POST"])
@login_required
@role_required(['admin', 'staff'])
def fee():
    db = get_db_connection()
    cursor = db.cursor()

    try:
        student_id = request.form["student_id"]
        fee_type = request.form["fee_type"]
        amount = request.form["amount"]

        cursor.execute("""
            INSERT INTO fee_detailstb
            (student_id, fee_type, amount, payment_date, receipt_no, payment_status)
            VALUES (%s, %s, %s, CURDATE(),
                    CONCAT('RCPT', FLOOR(RAND()*100000)), 'Paid')
        """, (student_id, fee_type, amount))

        db.commit()
        return jsonify({"status": "success", "message": "Fee Payment Successful!"}), 200
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass

# Hostel...........................................................................

@app.route("/hostel", methods=["POST"])
@login_required
@role_required(['admin', 'staff'])
def hostel():
    db = get_db_connection()
    cursor = db.cursor()

    try:
        student_id = request.form["student_id"]
        hostel_name = request.form["hostel_name"]
        room_no = request.form["room_no"]

        cursor.execute("""
            INSERT INTO hostel_allocationtb
            (student_id, hostel_name, room_no, allocation_date, status)
            VALUES (%s, %s, %s, CURDATE(), 'Allocated')
        """, (student_id, hostel_name, room_no))

        db.commit()
        return jsonify({"status": "success", "message": "Hostel Allocated Successfully!"}), 200
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass

#Exam......................................................................
@app.route("/exam", methods=["POST"])
@login_required
@role_required(['admin', 'staff'])
def exam():
    try:
        student_id = request.form["student_id"]
        semester = request.form["semester"]
        subject = request.form["subject"]
        marks = int(request.form["marks"])

        # Grade logic
        if marks >= 75:
            grade = 'A'
            result = 'Pass'
        elif marks >= 60:
            grade = 'B'
            result = 'Pass'
        elif marks >= 40:
            grade = 'C'
            result = 'Pass'
        else:
            grade = 'F'
            result = 'Fail'

        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        INSERT INTO exam_recordstb
        (student_id, semester, subject, marks, grade, result)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (student_id, semester, subject, marks, grade, result)

        cursor.execute(sql, values)
        db.commit()

        return jsonify({
            "status": "success",
            "message": "Exam Record Saved Successfully!",
            "grade": grade,
            "result": result
        }), 200
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass

#dashboarrd..........................................................

@app.route("/dashboard")
@login_required
@role_required(['admin'])
def dashboard():
    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM student_mastertb")
        total_students = cursor.fetchone()[0]

        cursor.execute("SELECT IFNULL(SUM(amount),0) FROM fee_detailstb")
        total_fees = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM hostel_allocationtb
            WHERE status='Allocated'
        """)
        hostel_occupied = cursor.fetchone()[0]

        return jsonify({
            "total_students": total_students,
            "total_fees": total_fees,
            "hostel_occupied": hostel_occupied
        }), 200
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass

#login......................................................................
@app.route("/login", methods=["POST"])
def login_route():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    username = request.form.get("username")
    password = request.form.get("password")

    try:
        cursor.execute("""
            SELECT * FROM userstb
            WHERE username=%s AND status='active'
        """, (username,))
        user = cursor.fetchone()
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            db.close()
        except Exception:
            pass

    if not user:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

    stored = user.get("password")
    # Ensure stored password is bytes for bcrypt.checkpw
    if isinstance(stored, (bytes, bytearray)):
        stored_pw = stored
    else:
        stored_pw = str(stored).encode('utf-8')

    try:
        if bcrypt.checkpw(password.encode('utf-8'), stored_pw):
            user_obj = User(user.get("user_id"), user.get("username"), user.get("role"))
            login_user(user_obj)
            return jsonify({"status": "success", "role": user.get("role"), "user_id": user.get("user_id")}), 200
        else:
            return jsonify({"status": "fail", "message": "Invalid credentials"}), 401
    except Exception as e:
        app.logger.exception("Error checking password for user %s", username)
        return jsonify({"status": "fail", "message": "Authentication error"}), 500

@app.route("/logout", methods=["POST"])
@login_required
def logout_route():
    logout_user()
    return jsonify({"status": "success", "message": "Logged out"}), 200

@app.route("/auth_check", methods=["GET"])
@login_required
def auth_check():
    """Check if user is authenticated and return role."""
    return jsonify({"status": "authenticated", "role": current_user.role, "username": current_user.username}), 200

#student dashboard............................................................................

@app.route("/student_dashboard")
@login_required
def student_dashboard():
    student_id = request.args.get("student_id")
    
    # Ensure students can only view their own data; admins can view any
    if current_user.role == 'student' and str(current_user.id) != str(student_id):
        return jsonify({"status": "fail", "message": "Unauthorized"}), 403

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT student_id, full_name, department, year
            FROM student_mastertb
            WHERE student_id=%s
        """, (student_id,))
        student = cursor.fetchone()

        cursor.execute("""
            SELECT fee_type, amount, payment_date
            FROM fee_detailstb
            WHERE student_id=%s
        """, (student_id,))
        fees = cursor.fetchall()

        cursor.execute("""
            SELECT hostel_name, room_no, status
            FROM hostel_allocationtb
            WHERE student_id=%s
        """, (student_id,))
        hostel = cursor.fetchone()

        return jsonify({
            "student": student,
            "fees": fees,
            "hostel": hostel
        }), 200
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            db.close()
        except:
            pass



if __name__ == "__main__":
    app.run(debug=True)
