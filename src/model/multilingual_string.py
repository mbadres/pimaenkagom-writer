from util.generator import generate_id


class String:
	"""
	This class represents a multilingual string.
	"""

	def __init__(self, empty=False):
		"""
		Constructor
		:param empty: A boolean, set true if you want to construct the empty string.
		"""
		self.__id = 0 if empty else generate_id()
		self.__status = "INCOMPLETE"
		self.__strings = {}

	def id(self):
		"""
		This method returns the id of the multilingual string.
		:return: An integer
		"""
		return self.__id

	def status(self):
		"""
		This method returns the status of the multilingual string.
		:return: A string
		"""
		return self.__status

	def strings(self):
		"""
		This method returns the all strings.
		:return: A dictionary
		"""
		return self.__strings

	def string(self, language):
		"""
		This method returns the string in the given language.
		:param language: A string
		:return: A string
		"""
		return self.__strings[language]

	def dict(self):
		"""
		This method returns the json string representation.
		:return: A dict
		"""
		return {
			"id": self.id(),
			"status": self.status(),
			"strings": self.strings()
		}

	def __str__(self):
		"""
		This method implements the string representation of the object.
		:return: A string
		"""
		return self.dict().__str__()

	def set_status(self, status):
		"""
		This method sets the status of the multilingual string.
		:param status: A string
		"""
		self.__status = status

	def set_string(self, language, string):
		"""
		This method sets a string in a given language.
		:param language: A string
		:param string: A string
		"""
		self.__strings[language] = string
