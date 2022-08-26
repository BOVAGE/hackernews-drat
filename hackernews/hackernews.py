import requests
from typing import List, Dict
import pprint
from utils import convert_unix_to_datetime
from exceptions import NotFound


class HackerNews:
    """
    A simple wrapper class for Hackernews API
    """

    base_url = "https://hacker-news.firebaseio.com/v0/"
    _item_url = f"{base_url}item/"
    top_stories_url = f"{base_url}topstories.json"
    ask_stories_url = f"{base_url}askstories.json"
    show_stories_url = f"{base_url}showstories.json"
    job_stories_url = f"{base_url}jobstories.json"
    max_item_id_url = f"{base_url}maxitem.json"
    single_item_url = _item_url + "{item_id}.json"

    def __init__(self):
        self.client = requests

    def _get_an_item(self, item_id: int) -> dict:
        """Get item with specified item_id

        Args:
            item_id (int): The item's id

        Returns:
            dictionary: a json format that representing info about the item
        """

        single_item_url = self.single_item_url.format(item_id=item_id)
        res = self.client.get(single_item_url)
        if res.json() is None:
            raise NotFound(f"Item with id:{item_id} not does not exist!")
        return res.json()

    def get_an_item(self, item_id: int, readable_time: bool = True) -> dict:
        """Get item with specified item_id

        Args:
            item_id (int): The item's id
            readable_time (bool): return datetime object for time key if True
            and if otherwise leave the unix timestamp as it is

        Returns:
            dictionary: a json format representing info about the item
        """
        data = self._get_an_item(item_id)
        if readable_time:
            data["time"] = convert_unix_to_datetime(data["time"])
        return data

    def _get_latest_item_id(self) -> int:
        """Get the id of the latest item

        Returns:
            int: An integer representing current largest item id
        """
        res = self.client.get(self.max_item_id_url)
        return res.json()

    def get_latest_item_id(self) -> dict:
        """Get the id of the latest item.

        Returns:
            data (dict): A key-value pair whose latest_item_id key has value of the largest item id
        """
        return {"latest_item_id": self._get_latest_item_id()}

    @property
    def latest_item_id(self) -> int:
        """returns the id of the latest item.

        Returns:
            latest_item_id(int): A  integer representing current largest item id
        """
        latest_item_id = int(self._get_latest_item_id())
        return latest_item_id

    def get_latest_items_ids(self, limit: int = 10):
        """Get the ids of the latest items in an iterable

        The ids are obtained based on walking backward from 'max-item id' returned from
        latest_item_id.

        Args:
            limit (int): Indicate the number of steps or count taken backward from
            the latest_item_id.

        Returns:
            generator (iterable): An object that can be iterated over to obtain the ids
            of last 'limit' added items
        """
        latest_item_id = self.latest_item_id
        count = 0
        while count < limit:
            count += 1
            prev_id = latest_item_id - count
            yield prev_id

    def get_top_500_stories(self) -> List[int]:
        """Get the id of the top and new 500 stories

        Returns:
            data (list): A list of integer representing the id of the item.
        """
        res = self.client.get(self.top_stories_url)
        return res.json()

    def get_ask_stories(self) -> List[int]:
        """Get the ids of 200 latest Show HN Stories.

        Returns:
            data (list): A list of integer representing the id of the item.
        """
        res = self.client.get(self.ask_stories_url)
        return res.json()

    def get_show_stories(self) -> List[int]:
        """Get the ids of 200 latest Show HN Stories.

        Returns:
            data (list): A list of integer representing the id of the item.
        """
        res = self.client.get(self.show_stories_url)
        return res.json()

    def get_job_stories(self) -> List[int]:
        """Get the ids of 200 latest Job HN Stories.

        Returns:
            data (list): A list of integer representing the id of the item.
        """
        res = self.client.get(self.job_stories_url)
        return res.json()


if __name__ == "__main__":
    h = HackerNews()
    # l = h.get_latest_items_ids()
    # print("generator", l)
    # print("iterator", iter(l))
    # print(type(iter(l)))
    # print("next", next(iter(l)))
    # for i in l:
    #     print(i)
    pprint.pprint(h.get_an_item(8863))
    # pprint.pprint(h.get_latest_item_id())
    # pprint.pprint(h.get_top_500_stories())
    # pprint.pprint(h.latest_item_id)
    # pprint.pprint(h.get_ask_stories())
    # pprint.pprint(h.get_show_stories())
    # pprint.pprint(h.get_job_stories())
