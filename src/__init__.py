from flask import Flask
from flask_login import LoginManager
from .config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user_bp.login'
    
    with app.app_context():
        from .models import User
        db.create_all()
        print('Database created')
    
    from src.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user/')
        
    return app
