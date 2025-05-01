from flask import Flask, render_template
import secrets

from .dbmanager import  init_db_command
from .home_view import bp as home_bp
from .address_views import bp as address_bp
from .address_api import bp as address_api


def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=secrets.token_urlsafe(32)
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    init_app(app)
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('custom404.html'), 404


    return app


def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(address_api)
    app.cli.add_command(init_db_command)

def cleanup(value):
    dbmanager.close_db()

