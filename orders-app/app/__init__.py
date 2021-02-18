from flask import Flask


def create_app(config='config.ProductionConfig'):
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    app.config.from_object(config)

    return app
