from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing_page.html')

@app.route("/home")
def home():
    return render_template('home.html', title='Home pag')

@app.route("/about")
def about():
    return render_template('about.html', title='About pag')


if __name__ == '__main__':
    app.run(debug=True)