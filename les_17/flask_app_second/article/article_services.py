from flask import request, render_template

from les_17.flask_app_second.article.models import Article


class ArticleService:
    session = None
    model = Article

    @classmethod
    def get_article_template(cls):
        return render_template('article/create.html')

    @classmethod
    def create_article(cls, session):
        try:
            header = request.form['article_header']
            content = request.form['article_content']

            article = cls.model(header=header, content=content)
            session.add(article)
            session.commit()
            return render_template('article/successfully_created.html')
        except Exception as e:
            raise e

    @classmethod
    def article_handler(cls, session):
        if request.method == 'GET':
            count_articles = session.query(Article).count()
            return f'Articles: {count_articles}<br><a href="/article/create-article">Create</a>'

        if request.method == 'POST':
            return cls.create_article(session)
