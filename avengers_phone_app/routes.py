from avengers_phone_app import app, db
from flask import render_template, request, url_for, redirect
from avengers_phone_app.forms import UserInfoForm, LoginForm

from avengers_phone_app.forms import UserInfoForm, LoginForm
from avengers_phone_app.models import User, check_password_hash

from flask_login import login_required, login_user, current_user, logout_user

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserInfoForm()

    if request.method == 'POST' and form.validate():
        #Get infor form the form & give them variable names
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        # print form inputs
        print(name, phone, email, password)

        user = User(name, phone, email, password)
        # Open a connection to the database
        db.session.add(user)
        # Commit all data to the database
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', user_form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user
        # and validate the password against the hash value
        # inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)