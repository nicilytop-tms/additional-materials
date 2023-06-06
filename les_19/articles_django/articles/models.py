from django.db import models


class Article(models.Model):
    header = models.CharField(max_length=255)
    content = models.TextField()


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()

    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
