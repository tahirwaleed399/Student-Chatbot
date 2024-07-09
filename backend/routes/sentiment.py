from flask import Blueprint, request, jsonify
from utils.error_handling import APIError
from services.sentiment_service import sentiment_service

bp = Blueprint('sentiment', __name__)

@bp.route('/sentiment', methods=['POST'])
def sentiment_route():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        raise APIError("No message provided", status_code=400)

    try:
        response = sentiment_service.analyze_sentiment(user_message)
        return jsonify({"response": response}), 200
    except Exception as e:
        raise APIError(f"Error analyzing sentiment: {str(e)}", status_code=500)
