from flask import Flask, render_template, url_for
from fakepinterest_proj import app
from flask_login import login_required
from fakepinterest_proj.forms import FormLogin, FormSignUp


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    return render_template('homepage.html', form=formlogin)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    formsignup = FormSignUp()
    return render_template('sign_up.html', form=formsignup)

@app.route('/profile/<given_user>')
@login_required
def profile(given_user):
    return render_template('profile.html', user=given_user)
