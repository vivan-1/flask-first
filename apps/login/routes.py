print('above blue')
from flask_login import current_user, login_user, login_required, logout_user
print('below current_user')
from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect
from apps.login.forms import regiteration, loginform
from apps.login.models import User
from apps import db

logger = Blueprint('logger', __name__)
print('below blue')



@logger.route('/')
def home():
    return render_template('home.html')

@logger.route('/register',methods=['GET', 'POST'])
def register():
    form = regiteration()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('registered successfully')
        return redirect (url_for('logger.login'))

    return render_template('register.html', form=form)

@logger.route('/login',methods=['GET', 'POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user.checkpassword( form.password.data) and user is not None:
            flash('invlaid credentials')
            return redirect(url_for('logger.login'))
        login_user(user)
        return redirect(url_for('calculate.calc'))
    return render_template('login.html', form=form)

@logger.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for('logger.home'))

@logger.app_errorhandler(404)
def pagenotfound(error):
    return render_template('404.html'), 404