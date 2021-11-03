from common.database import Database
from models.item import Item
from models.model import Model
import uuid


class Alert(Model):
	collection = "alerts"
	def __init__(self, item_id, price_limit, _id=None):
		self.item_id = item_id
		self.price_limit = price_limit
		self._id = _id or uuid.uuid4().hex
		self.item = Item.get_by_id(self._id)


	def json(self):
		return {
			"_id": self._id,
			"item_id": self.item_id,
			"price_limit": self.price_limits
		}


	def load_price(self):
		return self.item.load_price()


	def notify_if_price_reached(self):
		if self.load_price() < self.price_limit:
			return f"Item has reached a price under {self.price_limit} latest price {self.item.load_price()}"

