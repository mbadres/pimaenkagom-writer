import json

from tools.configuration import Configurator
from tools.generation import Generator


class Master:
	"""
	This class represents the manager and organizer of the model objects.
	"""

	def __init__(self):
		"""
		Constructor
		"""

		# initialize data storage
		self.multilingual_strings = {}

		self.clauses = {}
		self.lines = {}
		self.paragraphs = {}
		self.sections = {}
		self.chapters = {}
		self.parts = {}
		self.books = {}
		self.collections = {}

		# load config
		self.__config = Configurator("resources/config.yaml")

		collections = Generator.generate_library()
		library = []
		for collection in collections:
			library.append(collection.dict())
		file = open("sample-lib.json", "w")
		json.dump(library, file)

	def configurator(self):
		"""
		This method returns the configuration of the Master.
		:return: A configuration object
		"""
		return self.__config
