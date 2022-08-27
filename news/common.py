from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseItem(models.Model):
    """Base Item model that contains fields common to all item
    models.
    """

    class ItemType(models.TextChoices):
        """Enums for type of item"""

        JOB = _("Job")
        STORY = _("Story")
        COMMENT = _("Comment")
        POLL = _("Poll")
        POLLOPT = _("Poll Option")

    hnid = models.IntegerField(_("Hacker News Item Id"), db_index=True, unique=True)
    deleted = models.BooleanField(null=True, blank=True)
    type = models.CharField(choices=ItemType.choices, max_length=15)
    by = models.CharField(max_length=30)
    time = models.DateTimeField(null=True, blank=True)
    dead = models.BooleanField(null=True, blank=True)
    kids = models.JSONField(null=True, blank=True)
    is_api_created = models.BooleanField(default=False)

    class Meta:
        abstract = True
