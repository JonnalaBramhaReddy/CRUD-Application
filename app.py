from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jbramha@91",
    database="Registration"
)
app = Flask(__name__,
template_folder = "C:/Users/jbram/Desktop/Project/Assignment/templates")
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration")
    registrations = cursor.fetchall()
    return render_template('index.html', registrations=registrations)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        cursor = db.cursor()
        cursor.execute("INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (%s, %s, %s)", (name, email, dob))
        db.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration WHERE ID = %s", (id,))
    registration = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        cursor.execute("UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s WHERE ID = %s", (name, email, dob, id))
        db.commit()
        return redirect(url_for('index'))
    return render_template('update.html', registration=registration)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Registration WHERE ID = %s", (id,))
    db.commit()
    return redirect(url_for('index'))


if __name__ ==  "main":
        app.run(debug=True, port=5001)