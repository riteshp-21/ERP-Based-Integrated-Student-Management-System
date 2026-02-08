import mysql.connector
import bcrypt

# Adjust credentials if different from app.py
cfg = {
    'host': 'localhost',
    'user': 'root',
    'password': '3033',
    'database': 'student_erp_db'
}

username = 'admin'
password = 'admin123'  # change as desired

conn = mysql.connector.connect(**cfg)
cur = conn.cursor(buffered=True)
try:
    # Check if user exists
    cur.execute('SELECT user_id FROM userstb WHERE username=%s', (username,))
    row = cur.fetchone()
    if row:
        print('User already exists:', username)
    else:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cur.execute('INSERT INTO userstb (username, password, role, status) VALUES (%s, %s, %s, %s)',
                    (username, hashed.decode('utf-8'), 'admin', 'active'))
        conn.commit()
        print('Created user', username)
finally:
    try:
        cur.close()
    except Exception:
        pass
    try:
        conn.close()
    except Exception:
        pass

print('Done')
