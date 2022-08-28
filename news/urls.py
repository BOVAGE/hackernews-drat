from django.urls import path
from .views import home, search

app_name = "news"
urlpatterns = [
    path("", home, name="home"),
    path("search", search, name="search"),
]
