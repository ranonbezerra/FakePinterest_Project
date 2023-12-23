from flask import Flask, render_template, url_for
from fakepinterest_proj import app
from flask_login import login_required


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/profile/<given_user>')
@login_required
def profile(given_user):
    return render_template('profile.html', user=given_user)

