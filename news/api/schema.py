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
    story = graphene.Field(StoryType, hnid_or_id=graphene.Int(required=True))
    all_jobs = DjangoListField(JobType)
    job = graphene.Field(JobType, hnid_or_id=graphene.Int(required=True))
    all_comments = DjangoListField(CommentType)
    comment = graphene.Field(CommentType, hnid_or_id=graphene.Int(required=True))
    all_polls = DjangoListField(PollType)
    poll = graphene.Field(PollType, hnid_or_id=graphene.Int(required=True))
    all_poll_options = DjangoListField(PollOptionType)
    poll_option = graphene.Field(PollOptionType, hnid_or_id=graphene.Int(required=True))

    def resolve_story(self, info, hnid_or_id):
        story = Story.objects.filter(id=hnid_or_id).first()
        if not story:
            story = Story.objects.filter(hnid=hnid_or_id).first()
        return story

    def resolve_job(self, info, hnid_or_id):
        job = Job.objects.filter(id=hnid_or_id).first()
        if not job:
            job = Job.objects.filter(hnid=hnid_or_id).first()
        return job

    def resolve_comment(self, info, hnid_or_id):
        comment = Comment.objects.filter(id=hnid_or_id).first()
        if not comment:
            comment = Comment.objects.filter(hnid=hnid_or_id).first()
        return comment

    def resolve_poll(self, info, hnid_or_id):
        poll = Poll.objects.filter(id=hnid_or_id).first()
        if not poll:
            poll = Poll.objects.filter(hnid=hnid_or_id).first()
        return poll

    def resolve_poll_option(self, info, hnid_or_id):
        poll_option = PollOption.objects.filter(id=hnid_or_id).first()
        if not poll_option:
            poll_option = PollOption.objects.filter(hnid=hnid_or_id).first()
        return poll_option


class StoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        hnid = graphene.String(required=True)
        by = graphene.String(required=True)

    # The class attributes define the response of the mutation
    story = graphene.Field(StoryType)

    @classmethod
    def mutate(cls, root, info, hnid, by):
        story = Story.objects.create(hnid=hnid, by=by)
        # Notice we return an instance of this mutation
        return cls(story=story)


class Mutation(graphene.ObjectType):
    create_story = StoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
