from flask import Flask, render_template, url_for, redirect
from fakepinterest_proj import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest_proj.models import User, Post
from fakepinterest_proj.forms import FormLogin, FormSignUp


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        
        user = User.query.filter_by(email=form_login.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            
            login_user(user)
            return redirect(url_for('profile', user_id=user.id))

    return render_template('homepage.html', form=form_login)

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

        return redirect(url_for('profile', user_id=user.id))

    return render_template('sign_up.html', form=form_signup)

@app.route('/profile/<user_id>')
@login_required
def profile(user_id):

    
    
    if int(current_user().id) == int(user_id):
        return render_template('profile.html', user=current_user())
    else:
        user = User.query.get(int(user_id))
        return render_template('profile.html', user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
