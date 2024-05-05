import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def fetch_students():
    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    students = c.execute("SELECT * FROM students ORDER BY id DESC LIMIT 10").fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'gender': row[2], 'phone': row[3], 'email': row[4], 'address': row[5]} for
            row in students]


@app.route('/')
def index():
    module = 'master'
    return render_template('master.html', module=module)


@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module, data=fetch_students())


@app.route('/add_user')
def add_user():
    module = 'user'
    return render_template('add_user.html', module=module)


@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')

    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO students (user_name, gender, phone, email, address) VALUES (?, ?, ?, ?, ?)",
              (name, gender, phone, email, address))
    conn.commit()
    conn.close()
    return redirect(url_for('user'))


@app.route('/view_user')
def view_user():
    module = 'user'
    user_name = request.args.get('name')
    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    user = c.execute("SELECT * FROM students WHERE user_name=?", (user_name,)).fetchone()
    conn.close()
    print(f"User: {user}")
    return render_template('view_user.html', module=module, data=user)


@app.route('/confirm_delete_user')
def confirm_delete_user():
    module = 'user'
    user_id = request.args.get('id')
    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    user = c.execute("SELECT * FROM students WHERE id=?", (user_id,)).fetchone()
    conn.close()
    print(f"User: {user}")
    return render_template('confirm_delete_user.html', module=module, data=user)


@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form.get('id')
    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('user'))


@app.route('/edit_user')
def edit_user():
    module = 'user'
    user_id = request.args.get('id')
    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    user = c.execute("SELECT * FROM students WHERE id=?", (user_id,)).fetchone()
    conn.close()
    print(f"User: {user}")
    return render_template('edit_user.html', module=module, data=user)


@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')

    conn = sqlite3.connect('ss20_db.sqlite3')
    c = conn.cursor()
    c.execute("UPDATE students SET user_name=?, gender=?, phone=?, email=?, address=? WHERE id=?",
              (name, gender, phone, email, address, user_id))
    conn.commit()
    conn.close()
    return redirect(url_for('user'))


if __name__ == '__main__':
    app.run(debug=True)
