from flask import Blueprint, request, jsonify
from utils.error_handling import APIError
from services.langchain_service import langchain_service

bp = Blueprint('chat', __name__)

@bp.route('/chat', methods=['POST'])
def chat_route():
    data = request.json
    user_message = data.get('message')
    user_id = data.get('user_id')
    conversation_id = data.get('conversation_id')
    
    if not user_message or not user_id:
        raise APIError("No message or user ID provided", status_code=400)

    try:
        if not conversation_id:
            conversation_id = langchain_service.create_new_conversation(user_id)
        
        response = langchain_service.get_response(user_id, conversation_id, user_message)
        return jsonify({
            "response": response,
            "user_id": user_id,
            "conversation_id": conversation_id
        }), 200
    except Exception as e:
        raise APIError(f"Error generating response: {str(e)}", status_code=500)

@bp.route('/new_conversation', methods=['POST'])
def new_conversation():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        raise APIError("No user ID provided", status_code=400)

    try:
        conversation_id = langchain_service.create_new_conversation(user_id)
        return jsonify({
            "user_id": user_id,
            "conversation_id": conversation_id
        }), 200
    except Exception as e:
        raise APIError(f"Error creating new conversation: {str(e)}", status_code=500)