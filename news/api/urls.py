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

api_prefix = "api/v1/"
api_url_patterns = [
    path(f"{api_prefix}stories", StoryListCreateView, name="story"),
    path(f"{api_prefix}comments", CommentListCreateView, name="comment"),
    path(f"{api_prefix}jobs", JobListCreateView, name="job"),
    path(f"{api_prefix}polls", PollListCreateView, name="poll"),
    path(f"{api_prefix}pollopts", PollOptionListCreateView, name="pollopt"),
    path(f"{api_prefix}stories/<int:hnid>", StoryDetailView, name="story-detail"),
    path(f"{api_prefix}comments/<int:hnid>", CommentDetailView, name="comment-detail"),
    path(f"{api_prefix}jobs/<int:hnid>", JobDetailView, name="job-detail"),
    path(f"{api_prefix}polls/<int:hnid>", PollDetailView, name="poll-detail"),
    path(
        f"{api_prefix}pollopts/<int:hnid>", PollOptionDetailView, name="pollopt-detail"
    ),
]
