from flask import Blueprint

from les_17.flask_app_second.db import get_session
from les_17.flask_app_second.article.article_services import ArticleService

article_blueprint = Blueprint('article', __name__, template_folder='templates')


@article_blueprint.route('/', methods=['GET', 'POST'])
def get_articles():
    with get_session() as sess:
        return ArticleService.article_handler(sess)


@article_blueprint.route('/create-article', methods=['GET'])
def get_article_template():
    return ArticleService.get_article_template()
