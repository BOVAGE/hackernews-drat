from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Comment, Job, Poll, PollOption, Story
from .serializers import (
    CommentSerializer,
    JobSerializer,
    PollOptionSerializer,
    PollSerializer,
    StorySerializer,
)


class StoryListCreateView(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PollListCreateView(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Poll.objects.all()


class PollOptionListCreateView(generics.ListCreateAPIView):
    serializer_class = PollOptionSerializer
    queryset = PollOption.objects.all()


StoryListCreateView = StoryListCreateView.as_view()
CommentListCreateView = CommentListCreateView.as_view()
PollListCreateView = PollListCreateView.as_view()
JobListCreateView = JobListCreateView.as_view()
PollOptionListCreateView = PollOptionListCreateView.as_view()
