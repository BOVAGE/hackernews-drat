import logging

from celery import shared_task
from celery.schedules import crontab
from config.celery import app
from django.db import IntegrityError
from hackernews.hackernews import HackerNews
from .utils import save_item_to_db

logger = logging.getLogger(__name__)

hn = HackerNews()


@shared_task
def sync_new_item_from_hn():
    idx = hn.latest_item_id
    item = hn.get_an_item(idx)
    logger.info(f"saving item: hnid {idx}")
    try:
        instance = save_item_to_db(item)
    except IntegrityError as err:
        logger.warning(f"item with {idx} already exists")
    except Exception as err:
        logger.exception(f"An error occurred while saving {idx}")
    else:
        logger.info(f"saved item: hnid {idx} type: {instance.type} to db")


app.conf.beat_schedule = {
    # Executes at every five minutes
    "get-daily-bible-verse": {
        "task": "news.tasks.sync_new_item_from_hn",
        "schedule": crontab(minute="*/5"),
    },
}
