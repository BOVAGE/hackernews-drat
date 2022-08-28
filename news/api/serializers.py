from ..models import Story, Comment, Poll, Job, PollOption
from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = "__all__"
