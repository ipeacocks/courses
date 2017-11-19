#################
#### imports ####
#################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
import os

################
#### config ####
################

app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User, BlogPost

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    # # https://flask-login.readthedocs.org/en/latest/#flask.ext.login.LoginManager.user_loader
    # print "**********************"
    # # number in user.id dn
    # print user_id
    # # repr like <name admin>
    # print User.query.filter(User.id == int(user_id)).first()
    # # full query to db
    # print User.query.filter(User.id == int(user_id))
    # print "**********************"
    # return User.query.filter(User.id == int(user_id)).first()
    return User.query.filter_by(id=int(user_id)).first()