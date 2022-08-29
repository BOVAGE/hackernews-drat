from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from ..models import Comment, Job, Poll, PollOption, Story
from .serializers import (
    CommentSerializer,
    JobSerializer,
    PollOptionSerializer,
    PollSerializer,
    StorySerializer,
)
from .permissions import IsAPICREATEDORREADONLY


class StoryListCreateView(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()

    def perform_create(self, serializer):
        serializer.save(is_api_created=True)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(is_api_created=True)


class PollListCreateView(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    def perform_create(self, serializer):
        serializer.save(is_api_created=True)


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Poll.objects.all()

    def perform_create(self, serializer):
        serializer.save(is_api_created=True)


class PollOptionListCreateView(generics.ListCreateAPIView):
    serializer_class = PollOptionSerializer
    queryset = PollOption.objects.all()

    def perform_create(self, serializer):
        serializer.save(is_api_created=True)


class StoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAPICREATEDORREADONLY]
    queryset = Story.objects.all()
    lookup_field = "hnid"


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAPICREATEDORREADONLY]
    queryset = Comment.objects.all()
    lookup_field = "hnid"


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAPICREATEDORREADONLY]
    queryset = Job.objects.all()
    lookup_field = "hnid"


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollSerializer
    permission_classes = [IsAPICREATEDORREADONLY]
    queryset = Poll.objects.all()
    lookup_field = "hnid"


class PollOptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollOptionSerializer
    permission_classes = [IsAPICREATEDORREADONLY]
    queryset = PollOption.objects.all()
    lookup_field = "hnid"


StoryListCreateView = StoryListCreateView.as_view()
CommentListCreateView = CommentListCreateView.as_view()
PollListCreateView = PollListCreateView.as_view()
JobListCreateView = JobListCreateView.as_view()
PollOptionListCreateView = PollOptionListCreateView.as_view()

StoryDetailView = StoryDetailView.as_view()
CommentDetailView = CommentDetailView.as_view()
JobDetailView = JobDetailView.as_view()
PollDetailView = PollDetailView.as_view()
PollOptionDetailView = PollOptionDetailView.as_view()
