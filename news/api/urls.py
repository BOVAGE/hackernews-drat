from django.urls import path

from .views import (
    CommentListCreateView,
    JobListCreateView,
    PollListCreateView,
    PollOptionListCreateView,
    StoryListCreateView,
)

api_url_patterns = [
    path("stories", StoryListCreateView, name="story"),
    path("comments", CommentListCreateView, name="comment"),
    path("jobs", JobListCreateView, name="job"),
    path("polls", PollListCreateView, name="poll"),
    path("pollopts", PollOptionListCreateView, name="pollopt"),
]
