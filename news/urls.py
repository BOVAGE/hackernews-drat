from django.urls import path

from news.api.urls import api_url_patterns

from .views import home, search, detail

app_name = "news"
urlpatterns = [
    path("", home, name="home"),
    path("search", search, name="search"),
    path("<int:hnid>", detail, name="detail"),
] + api_url_patterns
