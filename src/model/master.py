from tools.configuration import Configurator


class Master:
	"""
	This class represents the manager and organizer of the model objects.
	"""

	def __init__(self):
		"""
		Constructor
		"""

		# load config
		self.__config = Configurator("resources/config.yaml")

	def configuration(self):
		"""
		This method returns the configuration of the Master.
		:return: A configuration object
		"""
		return self.__config
