from flask import render_template, url_for, flash, redirect, request
from predict import app, db, bcrypt
from predict.forms import RegistrationForm, LoginForm
from predict.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, You are now able to log in', 'success') # success is a bootstrap class
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') #next is set by login_manager                
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful, check email and password', 'danger')
    return render_template('login.html', form=form, title='Login')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
