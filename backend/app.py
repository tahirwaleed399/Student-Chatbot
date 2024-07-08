from flask import Flask
from flask_cors import CORS
from routes import chat, sentiment
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    app.register_blueprint(chat.bp)
    app.register_blueprint(sentiment.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()