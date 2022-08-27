from django.contrib import admin
from .models import Story, Job, Comment, Poll, PollOption


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["id", "hnid", "score", "descendants"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "hnid", "parent_model", "parent_object", "text"]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "hnid", "kids", "text"]


class PollOptionAdmin(admin.StackedInline):
    model = PollOption
    list_display = ["id", "hnid", "score"]


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["id", "hnid", "text", "descendants"]
    inlines = [PollOptionAdmin]
