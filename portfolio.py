"""
Main backe end module or routes script.
"""
from flask import Flask, render_template, url_for, flash, redirect
from forms import Sign_upForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c77bf579be8c14070701067f5240d22c'


@app.route("/")
def landing_page():
    return render_template('landing_page.html')

@app.route("/home")
def home():
    return render_template('home.html', title='Home pag')

@app.route("/about")
def about():
    return render_template('about.html', title='About pag')

@app.route("/sign_up")
def sign_up():
    form1 = Sign_upForm()
    if form1.validate_on_submit():
        flash(f'Account created for {form1.uname.data}!', 'success')
        return redirect(url_for('landing_page'))
    return render_template('sign_up.html', title='Sign up page', form=form1)



if __name__ == '__main__':
    app.run(debug=True)