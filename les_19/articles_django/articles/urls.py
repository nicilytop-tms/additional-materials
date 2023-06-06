from django.urls import path

from articles.views import ArticleView, get_articles, get_article, CommentView


urlpatterns = [
    path('', get_articles),
    path('article/', ArticleView.as_view()),
    path('article/<int:article_id>/', get_article),

    path('comment/', CommentView.as_view())
]
