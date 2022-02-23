from enum import Enum


class Layer(Enum):
	"""
	This class enumerates the types of a library node.
	"""

	LIBRARY = 0
	COLLECTION = 1
	BOOK = 2
	PART = 3
	CHAPTER = 4
	SECTION = 5
	PARAGRAPH = 6
	LINE = 7
	CLAUSE = 8

	@property
	def sublayer(self):
		"""
		This method returns the sublayer.
		"""
		return Layer(self.value + 1)
