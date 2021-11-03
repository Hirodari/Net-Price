from pymongo import MongoClient

class Database:

	uri = "mongodb+srv://hirodaridev:parkstreet02038%40@cluster0.nxudg.mongodb.net/test?"
	try:
		client = MongoClient(uri)
		db = client.microblog
	except:
		print("Unable to connect DB")

	@staticmethod
	def insert(collection, data):
		return Database.db[collection].insert_one(data)

	@staticmethod
	def find_one(collection, query):
		return Database.db[collection].find_one(query)

	@staticmethod
	def find(collection, query):
		return Database.db[collection].find(query)

	@staticmethod
	def remove(collection, query):
		return Database.db[collection].remove(query)

	@staticmethod
	def update(collection, query, data):
		return Database.db[collection].update(query, data, upsert=True)
