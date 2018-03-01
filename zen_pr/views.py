from django.contrib import auth

def home(request):
    username = auth.get_user(request).username

def show_article(request):
    username = auth.get_user(request).username