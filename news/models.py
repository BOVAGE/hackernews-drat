from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .common import BaseItem


class Comment(BaseItem):
    """Comment model"""

    type = models.CharField(default=BaseItem.ItemType.COMMENT, max_length=15)
    parent_model = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent_object = GenericForeignKey("parent_model", "parent_id")
    text = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.hnid}: type - {self.type}"


class Story(BaseItem):
    """Story model"""

    type = models.CharField(default=BaseItem.ItemType.STORY, max_length=15)
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    available_kids = GenericRelation(
        Comment, object_id_field="parent_id", content_type_field="parent_model"
    )

    def __str__(self):
        return f"{self.hnid}: type - {self.type}"

    class Meta:
        verbose_name_plural = "Stories"


class Job(BaseItem):
    """Job model"""

    type = models.CharField(default=BaseItem.ItemType.JOB, max_length=15)
    text = models.CharField(max_length=1000)
    available_kids = GenericRelation(
        Comment, object_id_field="parent_id", content_type_field="parent_model"
    )

    def __str__(self):
        return f"{self.hnid}: type - {self.type}"


class Poll(BaseItem):
    """Poll model"""

    type = models.CharField(default=BaseItem.ItemType.POLL, max_length=15)
    parts = models.JSONField(blank=True, null=True)
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=1000, null=True, blank=True)
    available_kids = GenericRelation(
        Comment, object_id_field="parent_id", content_type_field="parent_model"
    )

    def __str__(self):
        return f"{self.hnid}: type - {self.type}"


class PollOption(BaseItem):
    """Poll option model"""

    type = models.CharField(default=BaseItem.ItemType.POLLOPT, max_length=15)
    parent = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="available_parts"
    )
    score = models.IntegerField(blank=True, null=True)
    available_kids = GenericRelation(
        Comment, object_id_field="parent_id", content_type_field="parent_model"
    )

    def __str__(self):
        return f"{self.hnid}: type - {self.type}"
