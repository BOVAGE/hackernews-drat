from hackernews.hackernews import HackerNews
from .models import Story, Comment, Job, Poll, PollOption, BaseItem
import logging
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
from django.utils import timezone

hn = HackerNews()
ItemType = BaseItem.ItemType
logger = logging.getLogger(__name__)


def model_factory(item_type):
    """Returns the class of model based on item type"""
    model_instance_map = {
        ItemType.COMMENT: Comment,
        ItemType.STORY: Story,
        ItemType.JOB: Job,
        ItemType.POLL: Poll,
        ItemType.POLLOPT: PollOption,
    }
    item_type = item_type.title()
    if item_type not in model_instance_map:
        raise ValueError("Invalid item type")
    model = model_instance_map[item_type]
    return model


def model_to_use(item_type):
    """A wrapper function for model_factory.
    It adds error handling
    """
    model = None
    try:
        model = model_factory(item_type)
    except Exception as err:
        logger.exception("model not gotten")
    return model


def populate_100_items():
    """Seed database with 100 items
    NB: items added will be more than 100 because of the
    relationship that exist between items
    """
    ids = hn.get_latest_items_ids(100)
    for idx in ids:
        item = hn.get_an_item(idx)
        logger.info(f"saving item: hnid {idx}")
        try:
            instance = save_item_to_db(item)
        except IntegrityError as err:
            logger.warning("item with {idx} already exists")
        except Exception as err:
            logger.exception(f"An error occurred while saving {idx}")
        else:
            logger.info(f"saved item: hnid {idx} type: {instance.type} to db")


def save_item_to_db(item):
    """Save an item to the db,
    An item parent is also saved as well
    """
    data_to_save = format_item_for_db(item)
    item_type = data_to_save.pop("type")
    model = model_to_use(item_type)
    if does_item_exists_in_db(model, data_to_save["hnid"]):
        return model.objects.get(hnid=data_to_save["hnid"])
    print(f"model === {model} for {item_type}")
    parent_obj = None
    if "parent" in item:
        logger.info(f"{data_to_save} has parent")
        parent = get_parent_item(item)
        logger.info(f"parent item: {parent}")
        parent_obj = save_item_to_db(parent)

    instance = model(**data_to_save)
    if parent_obj:
        if model == PollOption:
            instance = model(**data_to_save, parent=parent_obj)
        elif model == Comment:
            parent_details = {
                "parent_model": ContentType.objects.get_for_model(parent_obj),
                "parent_id": parent_obj.id,
                "parent_object": parent_obj,
            }
            instance = model(**data_to_save, **parent_details)
    else:
        logger.info("No parent obj")
    instance.save()
    return instance


def get_parent_item(sub_item):
    """get the parent item of sub_item passed in"""
    parent_id = sub_item["parent"]
    item = hn.get_an_item(parent_id)
    return item


def format_item_for_db(item):
    """format the item dict to conform with the
    model field"""
    format_item = {**item}
    # to avoid passing by reference issue
    # item and format_item are two different dicts
    format_item["hnid"] = format_item.pop("id")
    format_item["time"] = timezone.make_aware(format_item.pop("time"))
    if "parent" in format_item:
        format_item.pop("parent")
    return format_item


def does_item_exists_in_db(model, hnid: int):
    """Check if the item passed already exist in the
    database based on the unique hind
    Args:
        model: model class to use
        hnid (dict): pass in the formatted Item data
    Return:
        item_exist (bool):  True / False
    """
    return model.objects.filter(hnid=hnid).exists()


def get_an_item_from_all_models(hnid):
    """get a single item from story, comment,
    job, poll, option models
    """
    item = None
    item = Story.objects.filter(hnid=hnid)
    if item:
        return item[0]
    item = Comment.objects.filter(hnid=hnid)
    if item:
        return item[0]
    item = Job.objects.filter(hnid=hnid)
    if item:
        return item[0]
    item = Poll.objects.filter(hnid=hnid)
    if item:
        return item[0]
    item = PollOption.objects.filter.get(hnid=hnid)
    if item:
        return item[0]


if __name__ == "__main__":
    populate_100_items()
