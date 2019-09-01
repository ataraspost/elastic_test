from django.contrib import admin
from article import models as articles_models


admin.site.register(articles_models.Article)

