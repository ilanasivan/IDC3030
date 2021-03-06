from item import Item
from errors import ItemNotExistError, ItemAlreadyExistsError


class ShoppingCart:

    def __init__(self):

        # Initialize subtotal
        self.subtotal = 0

        # Initialize cart dict
        self.dict = {}

        # Initialize list of tags
        self.tags = []

    def add_item(self, item: Item):
        """Add item to shopping cart

        Parameters:
        item (Item): The item to be added
        self: tags, dict, and subtotal

        Raises: ItemAlreadyExistError

        Updates:
        self : Hashtags, dict and subtotal plus the values of the item to be added
        """

        # If the item already exists in the cart throw an error
        if item.name in self.dict:
            raise ItemAlreadyExistsError

        # Otherwise add its price to the subtotal, add the item to the dict and add its tags to our list of total tags
        else:
            self.subtotal += item.price
            self.dict[item.name] = item
            self.tags += item.hashtags

    def remove_item(self, item_name: str):
        """Remove item from shopping cart

        Parameters:
        item_name (str): The name of the item to be removed
        self: tags, dict, and subtotal

        Raises: ItemNotExistError

        Updates:
        self : Hashtags, dict and subtotal less the values of the item to be removed
        """

        # If the item is in our dict then remove tags and remove the item from our dict and its price from the subtotal
        if item_name in self.dict:
            for i in self.dict[item_name].hashtags:
                self.tags.remove(i)
            self.subtotal -= self.dict.pop(item_name).price

        # Otherwise raise an error
        else:
            raise ItemNotExistError

    def get_subtotal(self) -> int:
        """Return the subtotal of the cart"""

        return self.subtotal
