from multilingual.language import Language
from multilingual.state import State
from tools.identifying import ID, generate_id


class String:
	"""
	This class represents a multilingual string.
	"""

	def __init__(self, empty: bool = False):
		"""
		Constructor
		:param empty: A boolean, set true if you want to construct the empty string.
		"""
		self.__id: ID = 0 if empty else generate_id()
		self.__state = State.INCOMPLETE
		self.__strings = {}

	@property
	def id(self) -> ID:
		"""
		This method returns the id of the multilingual string.
		:return: An ID
		"""
		return self.__id

	@property
	def state(self) -> State:
		"""
		This method returns the status of the multilingual string.
		:return: A state
		"""
		return self.__state

	@state.setter
	def state(self, value: State) -> None:
		"""
		This method sets the status of the multilingual string.
		:param value: A state
		"""
		self.__state = value

	@property
	def strings(self) -> {}:
		"""
		This method returns the all strings.
		:return: A dictionary
		"""
		return self.__strings

	def string(self, language: Language) -> str:
		"""
		This method returns the string in the given language.
		:param language: A language
		:return: A string
		"""
		return self.__strings[language]

	def set_string(self, language: Language, string: str) -> None:
		"""
		This method sets a string in a given language.
		:param language: A language
		:param string: A string
		"""
		self.__strings[language] = string

	def dict(self) -> {}:
		"""
		This method returns the json string representation.
		:return: A dict
		"""
		return {
			"id": self.id,
			"state": str(self.state),
			"strings": self.strings
		}

	def __str__(self) -> str:
		"""
		This method implements the string representation of the object.
		:return: A string
		"""
		return str(self.dict)
