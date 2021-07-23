import re
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 
import psycopg2.extras
import config

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

conn=psycopg2.connect(dbname=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, port=config.DB_PORT)


@app.route("/")
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sqlstr = "select * from students order by id"
    cur.execute(sqlstr)    
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@app.route("/add_student", methods=['POST'])
def add_student(): 
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        cur.execute("INSERT INTO students(fname,lname,email) VALUES(%s,%s,%s)",(fname,lname,email))
        conn.commit()
        flash('Student Added Successfully')
        return redirect(url_for('index'))

@app.route('/edit/<string:id>', methods=['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('select * from students where id = %s',(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', student=data[0])


@app.route('/update/<string:id>', methods=['POST'])
def update_student(id):
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            update students set fname=%s,lname=%s,email=%s where id=%s
        """, (fname,lname,email,id))
        flash('Student Updated Successfully')
        conn.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods=['POST','GET'])
def delete_student(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("DELETE FROM students where id = {0}".format(id))
    conn.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
