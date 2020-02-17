from django.urls import  path
from . import  views
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .models import Article
from .sitemaps import IndexSitemap,ArticleSitemap

app_name = "articles"

sitemaps = {
    'index': IndexSitemap,
    'articles': ArticleSitemap,
}


urlpatterns = [
    path('', views.index, name="index"),
    path('article/<int:article_id>',views.article_detail,name="article_detail"),
    path('<str:tag_name>',views.filter_by_tag,name="filter_by_tag"),
    path('aboutme/',views.myself,name="myself"),
    path('sortbydate/',views.sortByDate,name="sortbydate"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]