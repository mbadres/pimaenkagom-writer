from library.layer import Layer
from library.variety import Variety
from model.rule import Rule
from multilingual.string import String
from tools.identifying import ID, generate_id


class Node:
	"""
	This class represents an element in the library.
	"""

	def __init__(self, layer: Layer):
		"""
		TODO Extend constructor to be able to specify every property.
		TODO Support images.
		Constructor
		"""

		self.__id: ID = generate_id()
		self.__title: String = String(empty=True)
		self.__titled: bool = True
		self.__variety: Variety = Variety.NORMAL
		self.__layer: Layer = layer
		self.__audible: bool = True
		self.__visible: bool = True
		self.__icon: str = ""
		self.__rules: [] = []
		self.__children: [[Node]] = [[]]

	@property
	def id(self) -> ID:
		"""
		This method returns the id of the element.
		:return: An ID
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

	@property
	def variety(self) -> Variety:
		"""
		This method returns the element type.
		:return: A string
		"""
		return self.__variety

	@variety.setter
	def variety(self, value: Variety) -> None:
		"""
		This method sets the element type.
		:param value: A string
		"""
		self.__variety = value

	@property
	def layer(self) -> Layer:
		"""
		This method returns the element node type.
		:return: A node
		"""
		return self.__layer

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

	@property
	def rules(self) -> [Rule]:
		"""
		This method returns the rules.
		:return: A list
		"""
		return self.__rules

	@rules.setter
	def rules(self, value: [Rule]):
		"""
		This method sets the rules.
		:return: A list of rules
		"""
		self.__rules = value

	@property
	def children(self) -> list[list]:
		"""
		This method returns the children.
		:return: A list of lists
		"""
		return self.__children

	@children.setter
	def children(self, value: [[]]) -> None:
		"""
		This method sets the children.
		:param value: A list of lists
		"""
		for alternative in value:
			for child in alternative:
				if child.layer != self.layer.sublayer:
					raise Exception(f"ERROR: Children layer is not equal the sublayer of {self.layer.name}.")

		self.__children = value

	def dict(self) -> {}:
		"""
		This method returns the object's content in a dictionary.
		:return: A dict
		"""
		return {
			"id": self.id,
			"title": self.title.dict(),
			"titled": self.titled,
			"variety": str(self.variety),
			"layer": str(self.layer),
			"audible": self.audible,
			"visible": self.visible,
			"icon": self.icon,
			"rules": self.rules,
			"children": [[child.dict() for child in alternatives] for alternatives in self.children],
		}
