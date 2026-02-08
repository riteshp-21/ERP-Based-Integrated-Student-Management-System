import mysql.connector
import bcrypt

cfg = {
    'host': 'localhost',
    'user': 'root',
    'password': '3033',
    'database': 'student_erp_db'
}

username = 'admin'
new_password = 'admin123'

conn = mysql.connector.connect(**cfg)
cur = conn.cursor()
try:
    hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    cur.execute('UPDATE userstb SET password=%s WHERE username=%s', (hashed.decode('utf-8'), username))
    conn.commit()
    print('Password updated for', username)
finally:
    cur.close()
    conn.close()
