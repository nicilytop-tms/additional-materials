from flask import Flask

from les_17.flask_app_second.db import init_db
from les_17.flask_app_second.article.views import article_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    init_db(app)

    app.register_blueprint(article_blueprint, url_prefix='/article')
    return app
