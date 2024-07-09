from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code or 500
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response