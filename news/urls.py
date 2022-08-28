from django.urls import path

from news.api.urls import api_url_patterns

from .views import home, search

app_name = "news"
urlpatterns = [
    path("", home, name="home"),
    path("search", search, name="search"),
] + api_url_patterns
