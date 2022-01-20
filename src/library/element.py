from library.node import Node
from model.multilingual_string import String
from tools.generation import Generator


class Element:
	"""
	This class represents an element in the library.
	"""

	def __init__(self, node_type: Node = None):
		"""
		Constructor
		"""
		self.__id: int = Generator.generate_id()
		self.__title: String = String(empty=True)
		self.__titled: bool = True
		self.__type: str = ""
		self.__node_type: Node = node_type
		self.__audible: bool = True
		self.__visible: bool = True
		self.__icon: str = ""
		self.__version: int = 1
		self.__children: list[list[Element]] = [[]]

	def id(self) -> int:
		"""
		This method returns the id of the element.
		:return: An integer
		"""
		return self.__id

	def title(self) -> String:
		"""
		This method returns the title.
		:return: A multilingual string
		"""
		return self.__title

	def titled(self) -> bool:
		"""
		This method returns true if the element is titled.
		:return: A boolean
		"""
		return self.__titled

	def type(self) -> str:
		"""
		This method returns the element type.
		:return: A string
		"""
		return self.__type

	def node_type(self) -> Node:
		"""
		This method returns the element node type.
		:return: A string
		"""
		return self.__node_type

	def audible(self) -> bool:
		"""
		This method returns true if the element is set audible.
		:return: A boolean
		"""
		return self.__audible

	def visible(self) -> bool:
		"""
		This method returns true if the element is set visible.
		:return: A boolean
		"""
		return self.__visible

	def icon(self) -> str:
		"""
		This method returns the icon.
		:return: A string
		"""
		return self.__icon

	def version(self) -> int:
		"""
		This method returns the version.
		:return: An integer
		"""
		return self.__version

	def children(self) -> list[list]:
		"""
		This method returns the children.
		:return: A list of lists
		"""
		return self.__children
