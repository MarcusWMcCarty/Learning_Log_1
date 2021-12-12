from django.urls import path
from django.urls.resolvers import URLPattern

#. means same folder

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
]