from flask import Flask, render_template, url_for, redirect
from fakepinterest_proj import app, database, bcrypt
from flask_login import login_required, login_user, logout_user
from fakepinterest_proj.models import User, Post
from fakepinterest_proj.forms import FormLogin, FormSignUp


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    return render_template('homepage.html', form=formlogin)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form_signup = FormSignUp()

    if form_signup.validate_on_submit():

        password = bcrypt.generate_password_hash(form_signup.password.data).decode('utf-8')
        user = User(username=form_signup.username.data,
                    email=form_signup.email.data,
                    password=password)
        
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)

        return redirect(url_for('profile', given_user=user.username))


    return render_template('sign_up.html', form=form_signup)

@app.route('/profile/<given_user>')
@login_required
def profile(given_user):
    return render_template('profile.html', user=given_user)
