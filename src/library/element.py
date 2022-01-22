from library.node import Node
from multilingual.multilingual_string import String
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

	@property
	def id(self) -> int:
		"""
		This method returns the id of the element.
		:return: An integer
		"""
		return self.__id

	@property
	def title(self) -> String:
		"""
		This method returns the title.
		:return: A multilingual string
		"""
		return self.__title

	@title.setter
	def title(self, value: String) -> None:
		"""
		This method setts the title.
		:param value: A multilingual string
		"""
		self.__title = value
		self.__version += 1

	@property
	def titled(self) -> bool:
		"""
		This method returns true if the element is titled.
		:return: A boolean
		"""
		return self.__titled

	@titled.setter
	def titled(self, value: bool) -> None:
		"""
		This method sets the titled flag.
		:param value: A boolean
		"""
		self.__titled = value
		self.__version += 1

	@property
	def type(self) -> str:
		"""
		This method returns the element type.
		:return: A string
		"""
		return self.__type

	@type.setter
	def type(self, value: str) -> None:
		"""
		This method sets the element type.
		:param value: A string
		"""
		self.__type = value
		self.__version += 1

	@property
	def node_type(self) -> Node:
		"""
		This method returns the element node type.
		:return: A node
		"""
		return self.__node_type

	@property
	def audible(self) -> bool:
		"""
		This method returns true if the element is set audible.
		:return: A boolean
		"""
		return self.__audible

	@audible.setter
	def audible(self, value: bool) -> None:
		"""
		This method sets the audibility.
		:param value: A boolean
		"""
		self.__audible = value
		self.__version += 1

	@property
	def visible(self) -> bool:
		"""
		This method returns true if the element is set visible.
		:return: A boolean
		"""
		return self.__visible

	@visible.setter
	def visible(self, value: bool) -> None:
		"""
		This method sets the visibility.
		:param value: A boolean
		"""
		self.__visible = value
		self.__version += 1

	@property
	def icon(self) -> str:
		"""
		This method returns the icon.
		:return: A string
		"""
		return self.__icon

	@icon.setter
	def icon(self, value: str) -> None:
		"""
		This method sets the icon.
		:param value: A string
		"""
		self.__icon = value
		self.__version += 1

	@property
	def version(self) -> int:
		"""
		This method returns the version.
		:return: An integer
		"""
		return self.__version

	@property
	def children(self) -> list[list]:
		"""
		This method returns the children.
		:return: A list of lists
		"""
		return self.__children

	@children.setter
	def children(self, value: list[list]) -> None:
		"""
		This method sets the children.
		:param value: A list of lists
		"""
		self.__children = value
		self.__version += 1
