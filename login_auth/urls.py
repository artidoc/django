from django.conf.urls import url
from login_auth import views as login_views
from django.conf import settings

urlpatterns = [
    url(r'^$', login_views.login, name='login'),
    url(r'^logout/$', login_views.logout, name='logout'),
    url(r'^register/$', login_views.register, name='register'),
]