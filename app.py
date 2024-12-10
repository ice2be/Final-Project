from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection  # Import database connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = get_db_connection()
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Login validation
        sql = "SELECT * FROM Student WHERE email = %s AND password = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()

        if result:
            return render_template('user_info.html', user_data=result)
        else:
            return render_template('login.html', error="Invalid Username or Password")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        major = request.form.get('major')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        dob = request.form.get('dob')
        password = request.form.get('password')

        # Get the next available student ID
        cursor.execute("SELECT MAX(student_id) FROM Student")
        result = cursor.fetchone()
        max_student_id = result[0] if result[0] else 0
        student_id = max_student_id + 1

        # Insert new user into database
        sql = """INSERT INTO Student 
                 (student_id, Fname, Lname, major, address, phone_number, 
                 email, date_of_birth, password)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (student_id, fname, lname, major, address, phone, email, dob, password)
        cursor.execute(sql, values)
        db.commit()

        return render_template('register.html', message="Registration Successful! You can now log in.")
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
