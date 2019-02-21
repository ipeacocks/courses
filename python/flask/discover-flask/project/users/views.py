#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint # pragma: no cover
from flask.ext.login import login_user, login_required, logout_user # pragma: no cover
from form import LoginForm, RegisterForm # pragma: no cover
from project import db # pragma: no cover
from project.models import User, bcrypt # pragma: no cover

################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
) # pragma: no cover


################
#### routes ####
################

# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # first - is onle one element. all() is all elements from the db
            user = User.query.filter_by(name=form.username.data).first()

            # print "#--------"
            # print User.query.filter_by(name=request.form['username'])
            # print User.query.filter_by(name=request.form['username']).first()
            # print bcrypt.check_password_hash(user.password, request.form['password'])
            # print "#--------"

            if user is not None and bcrypt.check_password_hash(
                    user.password, form.password.data):
                # session['logged_in'] = True
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))                
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('users.login'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)
