from model.multilingual_string import String
from util.generator import generate_id


class Element:
	"""
	This class represents an element in the library.
	"""

	def __init__(self, node_type=None):
		"""
		Constructor
		"""
		self.__id = generate_id()
		self.__title = String(empty=True)
		self.__titled = True
		self.__type = None
		self.__node_type = node_type
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

	def type(self):
		"""
		This method returns the element type.
		:return: A string
		"""
		return self.__type

	def node_type(self):
		"""
		This method returns the element node type.
		:return: A string
		"""
		return self.__node_type

	def audible(self):
		"""
		This method returns true if the element is set audible.
		:return: A boolean
		"""
		return self.__audible

	def visible(self):
		"""
		This method returns true if the element is set visible.
		:return: A boolean
		"""
		return self.__visible

	def icon(self):
		"""
		This method returns the icon.
		:return: A string
		"""
		return self.__icon

	def version(self):
		"""
		This method returns the version.
		:return: An integer
		"""
		return self.__version

	def children(self):
		"""
		This method returns the children.
		:return: A list of lists
		"""
		return self.__children
