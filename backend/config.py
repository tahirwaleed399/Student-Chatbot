import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    FIRESTORE_CREDENTIALS = os.environ.get('FIRESTORE_CREDENTIALS')
    GEMINI_MODEL = 'gemini-pro'
    GEMINI_MAX_TOKENS = 1000
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}