from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a8916b4c43fa5d3629fe108c89c48992'

posts = [
    {
        'author': 'Svante Kumlien',
        'content': 'Lorem ipsum etc.',
        'title': 'Predictor might be alive!',
        'date_posted': '2020-04-06'
    },
    {
        'author': 'Svante Kumlien',
        'content': 'Lorem ipsum etc.',
        'title': 'Predictor is live!',
        'date_posted': '2020-04-07'
    }
]


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # success is a bootstrap class
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'svante.kumlien@gmail.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, check username and password', 'danger')
    return render_template('login.html', form=form, title='Login')


if __name__ == '__main__':
    app.run(debug=True)
