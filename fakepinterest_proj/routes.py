from flask import Flask, render_template, url_for, redirect, send_from_directory
from fakepinterest_proj import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest_proj.models import User, Post
from fakepinterest_proj.forms import FormLogin, FormSignUp, FormPost
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():
        
    if current_user.is_authenticated:
        return redirect(url_for('profile', user_id=current_user.id))
    
    else:
        form_login = FormLogin()

        if form_login.validate_on_submit():
            
            user = User.query.filter_by(email=form_login.email.data).first()
            
            if user and bcrypt.check_password_hash(user.password.encode('utf-8'), form_login.password.data):
                
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

@app.route('/profile/<user_id>', methods=['GET', 'POST'])
@login_required
def profile(user_id):

    if int(current_user.id) == int(user_id):
        form_post = FormPost()
        if form_post.validate_on_submit():
            print('oi')
            file = form_post.post_image.data
            safe_filename = secure_filename(file.filename)
            post_images_path = os.path.join(app.config["UPLOAD_FOLDER"], safe_filename)
            file.save(post_images_path)
            post = Post(image=safe_filename, user_id=int(current_user.id))
            database.session.add(post)
            database.session.commit()
            
        return render_template('profile.html', user=current_user, form=form_post)
    else:
        user = User.query.get(int(user_id))
        return render_template('profile.html', user=user, form=None)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route("/feed")
@login_required
def feed():
    posts = []

    for user_id in User.query.with_entities(User.id).all():
        if Post.query.filter_by(user_id = user_id[0]).order_by(Post.creation_date).all():
            last_user_post = Post.query.filter_by(user_id = user_id[0]).order_by(Post.creation_date).all()[-1]
            posts.append(last_user_post)
    if posts:
        return render_template("feed.html", posts=posts)
    else:
        return redirect(url_for('profile', user_id=current_user.id))
    
@app.route('/uploads/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    
