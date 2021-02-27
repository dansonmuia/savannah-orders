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

    from app.welcome import welcome
    app.register_blueprint(welcome)

    from app.auth import auth
    app.register_blueprint(auth)

    from app.customers import customers
    app.register_blueprint(customers, url_prefix='/customers')

    from app.orders import orders
    app.register_blueprint(orders, url_prefix='/orders')

    from app.http_error_handlers import error_handlers
    app.register_blueprint(error_handlers)

    return app
