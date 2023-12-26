from django.urls import path
from apps.base.views import index
# from django.conf.urls import handler404

urlpatterns = [
    path('<slug:slug>/', index, name='index'),
    path('', index, name='index_no_slug'), 


]

# handler404 = 'apps.base.views.errors'