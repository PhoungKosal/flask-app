import random

from flask import Flask, render_template, request

app = Flask(__name__)

names = ['Kosal', 'Nith', 'Sokha', 'Rithy', 'Sokun', 'Vannak', 'Sok', 'Sopheak', 'Meng', 'Chan']
genders = ['male', 'female']
addresses = ['Phnom Penh', 'Siem Reap', 'Battambang', 'Sihanoukville', 'Kampot', 'Kampong Cham', 'Kampong Thom',
             'Kratie', 'Preah Sihanouk', 'Koh Kong']

std_list = []

for i in range(1, 11):
    first_name = random.choice(names)
    email = f"{first_name.lower()}@gmail.com"
    student = {
        'id': i,
        'name': first_name,
        'gender': random.choice(genders),
        'phone': ''.join(random.choices('0123456789', k=10)),
        'email': email,
        'address': random.choice(addresses)
    }
    std_list.append(student)


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
