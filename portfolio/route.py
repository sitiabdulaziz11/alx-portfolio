from flask import render_template, url_for, flash, redirect, request
from portfolio.forms import Sign_upForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from portfolio import app, db, bcrypt
from portfolio.models import User


@app.route("/")
def landing_page():
    return render_template('landing_page.html')

@app.route("/home")
def home():
    return render_template('home.html', title='Home pag')

@app.route("/about")
def about():
    return render_template('about.html', title='About pag')

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    form1 = Sign_upForm()
    if form1.validate_on_submit():
         user = User(username=form1.username.data, email=form1.email.data, password=form1.password.data)
         db.session.add(user)
         db.session.commit()
         flash(f'Your Account has ben created! You are now able to log in', 'success')
         return redirect(url_for('landing_page'))
    return render_template('sign_up.html', title='Sign up page', form=form1)

@app.route("/login", methods=['GET', 'post'])
def login():
    form2 = LoginForm()
    if form2.validate_on_submit():
        user = User.query.filter_by(email=form2.email.data).first()
    return render_template('login.html', title='Login', form=form2)