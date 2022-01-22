import uuid
from random import randint, choice

from model.library import Library
from multilingual.multilingual_string import String


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
		This static method generates a random id.
		:return: A 64-bit integer
		"""
		maxint64 = (1 << 64) - 1
		randint128 = uuid.uuid4().int
		return maxint64 & randint128

	@staticmethod
	def generate_words(consonants: [str] = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
	                   vowel: [str] = ["a", "e", "i", "o", "u"]) -> str:
		"""
		This static method generates a random word.
		:param consonants: A list of strings
		:param vowel: A list of strings
		:return: A string.
		"""

		# set constants for the randomisation engine
		min_number_letters: int = 1
		max_number_letters: int = 14

		# determine the word length
		length = randint(min_number_letters, max_number_letters)

		# store the result
		word = ""

		# construct the word
		for _ in range(length):
			word += choice(consonants)
			word += choice(vowel)

		return word

	@staticmethod
	def generate_string() -> String:
		"""
		TODO implement
		This static method generates a random multilingual string.
		:return: A multilingual string.
		"""

		# set constants for the randomisation engine
		min_number_words: int = 3
		max_number_words: int = 14



		return String(empty=True)

	@staticmethod
	def generate_library() -> Library:
		"""
		TODO implement
		This static method generates a random library.
		:return: A library.
		"""
		return Library()
