from common.database import Database
from models.model import Model
from bs4 import BeautifulSoup
import uuid
import requests

class Item(Model):
	collection = "items"
	def __init__(self,uri,tag,query, _id=None):
		self.uri = uri
		self.tag = tag
		self.query = query
		self._id = _id or uuid.uuid4().hex
		# self.db = Database()
		self.collection = "items"

	def json(self):
		return {
			"_id": self._id,
			"uri": self.uri,
			"tag": self.tag,
			"query": self.query
		}

	def page_gen(self):
		yield requests.get(self.uri).content

	def load_price(self):
		soup = BeautifulSoup(next(self.page_gen()), "html.parser")
		price = soup.find(self.tag, self.query).get_text(strip=True)
		if len(price) > 10:
			self.price = re.findall(r'[\d]+[.,\d]+', price)[-1]
			return float(self.price)
		else:
			self.price = float(price[1:].replace(",", ""))
			return self.price

