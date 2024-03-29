from flask import render_template, url_for, flash, redirect, request, Response
from portfolio.forms import Sign_upForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from portfolio import app, db, bcrypt
from portfolio.models import User


@app.route("/")
@app.route('/index.html')
def index():
    html_content =  render_template('index.html')
    response = Response(html_content, content_type='text/html')
    return response

@app.route("/home.html")
def home():
    return render_template('home.html', title='Home pag')

@app.route("/about.html")
def about():
    return render_template('about.html', title='About pag')

@app.route("/contact.html")
def contact():
    return render_template('contact.html', title='contact pag')

@app.route("/sign_up.html", methods=['GET', 'POST'])
def sign_up():
    form1 = Sign_upForm()
    if form1.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form1.password.data).decode('utf-8')
        user = User(username=form1.username.data, email=form1.email.data, password=hashed_password)
        """user = User(username=form1.username.data, email=form1.email.data, password=form1.password.data)""" # this is for unhashed plain text password
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has ben created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign up page', form=form1)

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    form2 = LoginForm()
    if form2.validate_on_submit():
        user = User.query.filter_by(email=form2.email.data).first()
        return render_template(url_for('home'), title='Login', form=form2)
    return render_template('login.html', title='Login', form=form2)