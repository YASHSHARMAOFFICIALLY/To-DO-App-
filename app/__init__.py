from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from main import main_bp
db = SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Yash"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    


    app.config['SESSION_COOKIE_SAMESITE'] = "Lax"
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    from main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(main_bp)
    return app


@login_manager.user_loader
def load_user(user_id):
    from app.model import users
    return users.query.get(int(user_id))


