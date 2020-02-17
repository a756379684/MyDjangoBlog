from django.contrib import sitemaps
from django.urls import reverse
from .models import Article

class IndexSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self,obj):
        return reverse("articles:index")

class ArticleSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.create

    def location(self,obj):
        return reverse("articles:article_detail",args=(obj.id,))