from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^$', views.matrix, name='matrix'),
]