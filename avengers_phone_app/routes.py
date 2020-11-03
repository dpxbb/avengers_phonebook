from avengers_phone_app import app
from flask import render_template, request
from avengers_phone_app.forms import UserInfoForm

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

    return render_template('register.html', user_form = form)