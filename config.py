import os

class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=a63377ab71ed40e0b9ed31f548300b72'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):

    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}