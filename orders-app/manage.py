import os

from app import create_app


config_map = {'development': 'config.DevelopmentConfig',
              'production': 'config.ProductionConfig',
              'testing': 'config.TestingConfig'
              }

env = config_map.get(os.environ.get('FLASK_ENV'), 'config.ProductionConfig')

app = create_app(env)
