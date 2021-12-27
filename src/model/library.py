from model.multilingual_string import String
from util.generator import generate_id


class Element:
	"""
	This class represents an element in the library
	"""

	def __init__(self):
		"""
		Constructor
		"""
		self.__id = generate_id()
		self.__title = String(empty=True)
		self.__titled = True
		self.__type = None
		self.__node_type = None
		self.__audible = True
		self.__visible = True
		self.__icon = ""
		self.__version = 1
		self.__children = [[]]

	def id(self):
		"""
		This method returns the id of the element.
		:return: An integer
		"""
		return self.__id

	def title(self):
		"""
		This method returns the title.
		:return: A multilingual string
		"""
		return self.__title

	def titled(self):
		"""
		This method returns true if the element is titled.
		:return: A boolean
		"""
		return self.__titled


class Library:
	"""
	This class represents a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""

		# store multilingual strings
		self.multilingual_strings = []

		# store library elements
		self.clauses = []
		self.lines = []
		self.paragraphs = []
		self.sections = []
		self.chapters = []
		self.parts = []
		self.books = []
		self.collections = []
