from model.multilingual_string import String
from util.generator import generate_id


class Element:
	"""
	This clas represents an element in the library
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


class Library:
	""""""

	def __init__(self):
		""""""

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
