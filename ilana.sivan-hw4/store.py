import yaml

from errors import ItemAlreadyExistsError, ItemNotExistError, TooManyMatchesError
from item import Item
from shopping_cart import ShoppingCart


def sort_tags(item: Item, tags: list):
    """Adds hashtags that are common to a list called mutual_tags

    Parameters:
    item (Item): the item whose tags we are checking
    tags (list): the list of tags

    Returns:
    The length of the list mutual_tags
    """

    # Initialize list of mutual tags
    mutual_tags = []

    # Iterate
    for hashtag in tags:

        # If the hashtag is in the item's hashtags add it to the mutual list
        if hashtag in item.hashtags:
            mutual_tags.append(hashtag)

    # Return the list
    return len(mutual_tags)


def find_name(item: Item):
    # Return the item name
    return item.name


class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()
        self.hashtags = []

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    def search_by_name(self, item_name: str) -> list:
        """Return a sorted list of all the items that match item_name

        Parameters:
        item_name (str): The name of the item to be removed
        self: shopping_cart.dict, shopping_cart.tags

        Returns:
        The sorted list called items
        """
        # Pull the names from the shopping cart dict
        item_names = self._shopping_cart.dict.keys()

        # Compile a list of items that exist in the store but are not in the cart where x is the item
        items = [x for x in self._items if x.name.find(item_name) != -1 and x.name not in item_names]

        # Sort for y using sort_tags and find_name, using y as item and tags
        items.sort(key=lambda y: (-sort_tags(y, self._shopping_cart.tags), find_name(y)))

        # Return sorted items
        return items

    def search_by_hashtag(self, hashtag: str) -> list:
        """Return a sorted list of all items with matching hashtags

        Parameters:
        hashtag (str): The hashtag of interest
        self: shopping_cart.dict, shopping_cart.tags

        Returns:
        The sorted list called items
        """

        # Pull the names from the shopping cart dict
        item_names = self._shopping_cart.dict.keys()

        # Compile a list of values where the item is in the items and the hashtag matches the item's hashtags
        items = [x for x in self._items if hashtag in x.hashtags and x.name not in item_names]

        # Sort
        items.sort(key=lambda item: (-sort_tags(item, self._shopping_cart.tags), find_name(item)))

        # Return items matching
        return items

    def add_item(self, item_name: str):
        """Add item to shopping cart

        Parameters:
        item_name (str): The name of the item to be removed
        self: Hashtags, dict, and subtotal

        Raises: ItemNotExistError

        Updates:
        self : Hashtags, dict and subtotal less the values of the item to be removed
        """

        # Search by the name
        items = self.search_by_name(item_name)

        # Raise error if there is more than one matching item
        if len(items) > 1:
            raise TooManyMatchesError

        # Check for item's existence
        elif not any(item.name.find(item_name) != -1 for item in self._items):
            raise ItemNotExistError

        # Raise an error if the item was already added
        elif len(items) == 0:
            raise ItemAlreadyExistsError

        else:

            # Add item using the method from shopping cart
            self._shopping_cart.add_item(items[0])

    def remove_item(self, item_name: str):
        """Remove item

        Parameters:
        item_name (str): The name of the item to be removed
        self: specifically the shopping_cart

        Raises: ItemNotExistError, TooManyMatchesError

        Updates:
        self : shopping cart
        """

        # Create a list of all the items in the cart where the item name is in their name
        items = [items_in_cart for items_in_cart in self._shopping_cart.dict.keys() if
                 items_in_cart.find(item_name) != -1]

        # Raise error if there is more than one matching item
        if len(items) > 1:
            raise TooManyMatchesError

        # Check for item in self._items if the boolean created by any() is true and therefore not in the cart, or if items is empty
        elif len(items) == 0 or not any(item.name.find(item_name) != -1 for item in self._items):
            raise ItemNotExistError

        # Remove items
        self._shopping_cart.remove_item(items[0])

    def checkout(self) -> int:
        """Return total"""
        return self._shopping_cart.get_subtotal()
