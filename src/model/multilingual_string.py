from util.generator import generate_id


class String:
	"""
	This class represents a multilingual string.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		self.__id = generate_id()
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
		This method returns the status of the multilingual string
		:return: A string
		"""
		return self.__status

	def strings(self):
		"""
		This method returns the all strings
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

	def set_status(self, status):
		"""
		This method sets the status of the multilingual string.
		:param status: A string
		"""
		self.__status = status

	def set_string(self, language, string):
		"""
		This method
		:param language:
		:param string:
		:return:
		"""
		self.__strings[language] = string
