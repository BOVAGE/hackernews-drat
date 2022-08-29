from news.models import Story, Job, Comment, Poll, PollOption
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField


class StoryType(DjangoObjectType):
    class Meta:
        model = Story
        fields = "__all__"


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = "__all__"


class JobType(DjangoObjectType):
    class Meta:
        model = Job
        fields = "__all__"


class PollType(DjangoObjectType):
    class Meta:
        model = Poll
        fields = "__all__"


class PollOptionType(DjangoObjectType):
    class Meta:
        model = PollOption
        fields = "__all__"


class Query(graphene.ObjectType):
    all_stories = DjangoListField(StoryType)
    all_jobs = DjangoListField(JobType)
    all_comments = DjangoListField(CommentType)
    all_polls = DjangoListField(PollType)
    all_poll_options = DjangoListField(PollOptionType)


schema = graphene.Schema(query=Query)
