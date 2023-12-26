from django.contrib.sitemaps import Sitemap
from apps.base.models import Index

class IndexSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Index.objects.all()
    
    def lastmod(self, obj):
        pass