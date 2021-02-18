from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config='config.ProductionConfig'):
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.customers import customers
    app.register_blueprint(customers, url_prefix='/customers')

    return app
