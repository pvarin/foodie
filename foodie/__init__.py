import os
from flask import Flask, render_template
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    testing = False
    if testing:
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object(os.environ['APP_SETTINGS'])

    from foodie.database import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from foodie import models
    
    @app.route('/')
    def main():
        return render_template('index.html')
    
    from foodie.recipes import recipes
    app.register_blueprint(recipes, url_prefix="/recipes")

    return app
