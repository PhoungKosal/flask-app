import random

from flask import Flask, render_template, request
import  sqlite3

app = Flask(__name__)

std_list = []

cnn = sqlite3.connect('ss20_db.sqlite3')
cour = cnn.cursor()
students = cour.execute("""SELECT * FROM students limit 10""")
for row in students:
    std_list.append({
        'id': row[0],
        'name': row[1],
        'gender': row[2],
        'phone': row[3],
        'email': row[4],
        'address': row[5]
    })


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
    return render_template('user.html', module=module, data=std_list)


@app.route('/add_user')
def add_user():
    module = 'user'
    return render_template('add_user.html', module=module, data=std_list)

@app.post('/create_user')
def create_user():
    module = 'user'
    id = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    user ={
        'name': name,
        'gender': gender,
        'phone': phone,
        'email': email,
        'address': address
    }
    return user


@app.route('/view_user')
def view_user():
    module = 'user'
    current_user = request.args.get('name', default='all', type=str)
    user_dict = filter(lambda x: x['name'] == current_user, std_list)
    user_list = list(user_dict)
    return render_template('view_user.html', module=module, data=user_list[0])


@app.route('/confirm_delete_user')
def confirm_delete_user():
    module = 'user'
    current_user = request.args.get('name', default='all', type=str)
    user_dict = filter(lambda x: x['name'] == current_user, std_list)
    user_list = list(user_dict)
    return render_template('confirm_delete_user.html', module=module, data=user_list[0])


@app.route('/edit_user')
def edit_user():
    module = 'user'
    current_user = request.args.get('id', default='all', type=int)
    user_dict = filter(lambda x: x['id'] == current_user, std_list)
    user_list = list(user_dict)
    return render_template('edit_user.html', module=module, data=user_list[0])


# @app.route('/edit_user/<int:user_id>')
# def edit_user(user_id):
#     module = 'user'
#     user_id = user_id
#     current_user = []
#     for item in std_list:
#         if user_id == item['id']:
#             current_user = item
#     return render_template('edit_user.html', module=module, data=current_user)


if __name__ == '__main__':
    app.run()
