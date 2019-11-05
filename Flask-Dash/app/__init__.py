from flask import Flask
import dash
from config import config
from .dash_application import dash_example

dash = dash_example.dash_application()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # This is where a dash app attaches to a server
    dash.init_app(app=app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
