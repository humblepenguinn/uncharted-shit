from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "teams.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .models import Team

    if not path.exists('website/'+DB_NAME):
        with app.app_context(): db.create_all()
        print("Created Database!")

    app.register_blueprint(views, url_prefix='/')

    return app

