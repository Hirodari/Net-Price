from abc import ABCMeta, abstractmethod
from common.database import Database

class Model(metaclass=ABCMeta):

	@abstractmethod
	def json(self):
		raise NotImplementedError

	def save_to_mongo(self):
		print(self.json())
		if Database.insert(self.collection, self.json()):
			return "Data inserted!"
		return "check the DB connection"

	@classmethod
	def all(cls):
		return [cls(**item) for item in Database.find(cls.collection, {})]

	@classmethod
	def find_one(cls, attribute, value):
		print(attribute, value)
		return cls(**Database.find_one(cls.collection, {attribute: value}))

	@classmethod
	def get_by_id(cls,id):
		return cls.find_one("_id", id)

	@classmethod
	def find_many(cls, query):
		return [cls(**item) for item in Database.find(cls.collection, query)]

	@classmethod
	def remove_from_mongo(cls, id):
		print(cls.collection, id)
		return Database.remove(cls.collection,{"_id": id})