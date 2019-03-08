from flask import render_template, url_for, flash, redirect, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskapp.models.users import User
from flaskapp.models.cards import Card
from flask_login import login_user, current_user, logout_user, login_required

# Dummy Data
cards = [
    {
        'name': 'Archangel Avacyn',
        'types': [
            'Creature'
        ],
        'subtypes': [
            'Angel'
        ],
        'power': '4', 
        'toughness': '4',
        'manaCost': '{3}{W}{W}'
    }
]

@app.route("/")
def home():
    cards = Card.query.all()
    return render_template('index.html', cards=cards)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for %s!' % form.username.data, 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    return render_template('account.html', title='Account', form=form)

@app.route("/upload")
@login_required
def upload():
    return render_template('upload.html')

@app.route("/card-list")
@login_required
def cardList():
    return render_template('card-list.html', cards=cards)