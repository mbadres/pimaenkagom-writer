import yaml

from util.observation import Observable


class Configuration(Observable):
	"""
	This class represents a configuration file
	"""

	def __init__(self, path):
		"""
		Constructor
		:param path: The file path as a string
		"""
		super().__init__()
		self.__path = path
		self.__settings = yaml.safe_load(open(path, "r"))

	def get(self, key):
		"""
		This method returns a specific setting.
		:return: This may be an integer, a string or an array.
		"""
		return self.__settings[key]

	def get_all(self):
		"""
		This method returns all settings.
		:return: A dictionary
		"""
		return self.__settings

	def set(self, key, value):
		"""
		This method sets a setting.
		:param key: A string
		:param value: This may be an integer, a string or an array.
		"""
		self.__settings[key] = value
		self.save()
		self.notify()

	def save(self):
		"""
		This method stores the configuration in the corresponding file.
		"""
		yaml.dump(self.__settings, open(self.__path, "w"))
