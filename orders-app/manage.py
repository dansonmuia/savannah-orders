import os

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app import create_app


config_map = {'development': 'config.DevelopmentConfig',
              'production': 'config.ProductionConfig',
              'testing': 'config.TestingConfig'
              }

env = config_map.get(os.environ.get('FLASK_ENV'), 'config.ProductionConfig')

app = create_app(env)


@app.cli.command('fly-init-db')
def fly_init_db():
    url = app.config['SQLALCHEMY_DATABASE_URI']

    engine = create_engine(url, echo=True)
    print('Checking db')
    if not database_exists(engine.url):
        create_database(engine.url)
        print('Database not found. Created a new one')
    else:
        print('Database Found')
