from django.urls import path

from .views import (
    CommentListCreateView,
    JobListCreateView,
    PollListCreateView,
    PollOptionListCreateView,
    StoryListCreateView,
    StoryDetailView,
    CommentDetailView,
    JobDetailView,
    PollDetailView,
    PollOptionDetailView,
)

urlpatterns = [
    path("stories", StoryListCreateView, name="story"),
    path("comments", CommentListCreateView, name="comment"),
    path("jobs", JobListCreateView, name="job"),
    path("polls", PollListCreateView, name="poll"),
    path("pollopts", PollOptionListCreateView, name="pollopt"),
    path("stories/<int:hnid>", StoryDetailView, name="story-detail"),
    path("comments/<int:hnid>", CommentDetailView, name="comment-detail"),
    path("jobs/<int:hnid>", JobDetailView, name="job-detail"),
    path("polls/<int:hnid>", PollDetailView, name="poll-detail"),
    path("pollopts/<int:hnid>", PollOptionDetailView, name="pollopt-detail"),
]
