import flask
from flask_cors import CORS
from routes.chat import bp as chat_bp
from routes.sentiment import bp as sentiment_bp
from config import config
from utils.error_handling import APIError, handle_api_error
from dotenv import load_dotenv
import os 
load_dotenv()

def create_app(config_name='default'):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    app.register_blueprint(chat_bp, url_prefix='/api')
    app.register_blueprint(sentiment_bp, url_prefix='/api')

    app.register_error_handler(APIError, handle_api_error)
    @app.route('/')
    def hello_world():
        print('Walee dThair ')
        print(os.getenv('GEMINI_API_KEY'))

        return flask.jsonify(message="Hello World"), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
