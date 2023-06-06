from django.views import View
from django.shortcuts import render, redirect

from articles.models import Article, Comment


def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', context={'articles': articles})


class ArticleView(View):
    def get(self, request):
        return render(request, 'article-create.html', context={'action_path': '/article/'})

    def post(self, request):
        header = request.POST.get('article_header')
        content = request.POST.get('article_content')

        Article.objects.create(header=header, content=content)
        return render(request, 'article-created.html')


class CommentView(View):
    def post(self, request):
        user_name = request.POST.get('user_name')
        message = request.POST.get('message')
        article_id = request.POST.get('article_id')

        article = Article.objects.get(id=article_id)

        Comment.objects.create(user_name=user_name, message=message, article_id=article)

        return redirect(f'/article/{article_id}')


def get_article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    return render(request, 'article.html', context={'article': article, 'comments': comments, 'action_path': '/comment/'})
