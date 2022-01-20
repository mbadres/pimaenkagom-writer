import uuid

from model.library import Library
from model.multilingual_string import String


class Generator:
	"""
	This class represents a generator for ids, sample strings and libraries.
	"""

	def __init__(self):
		"""
		Constructor
		"""

	@staticmethod
	def generate_id() -> int:
		"""
		This method generates a random id.
		:return: A 64-bit integer
		"""
		maxint64 = (1 << 64) - 1
		randint128 = uuid.uuid4().int
		return maxint64 & randint128
