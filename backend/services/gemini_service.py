import os
import google.generativeai as genai
from google.api_core import retry
from google.api_core import exceptions

# Configure the Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class GeminiService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.0-pro-latest')

    @retry.Retry(predicate=retry.if_exception_type(
        exceptions.ServiceUnavailable,
        exceptions.ResourceExhausted,
        exceptions.InternalServerError
    ))
    def generate_response(self, prompt, max_tokens=1000):
      
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except exceptions.GoogleAPIError as e:
            print(f"Gemini API error: {e}")
            raise

gemini_service = GeminiService()