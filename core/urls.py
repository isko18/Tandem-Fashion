"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from apps.base.sitemap import IndexSitemap
from django.views.generic import TemplateView
# from apps.base.views import quiz_submission

sitemaps = {
    'index' : IndexSitemap
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.base.urls")),
    re_path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path('robots.txt', TemplateView.as_view(template_name = "robots.txt", content_type = "text/pali")),
    # re_path('quiz_submission/', quiz_submission, name='quiz_submission'),


    # path('', include("apps.telegram.urls")),


]

handler404 = 'apps.base.views.errors'


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)