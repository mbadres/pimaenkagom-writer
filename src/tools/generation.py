from random import randint, choice

from library.layer import Layer
from library.node import Node
from multilingual.state import State
from multilingual.string import String


class Generator:
	"""
	This class represents a generator for ids, sample strings and libraries.
	"""

	@staticmethod
	def __random_length(min_number: int = 3, max_number: int = 14) -> int:
		"""
		This static method generates an integer between 3 and 14.
		:param min_number: An integer
		:param max_number: An integer
		:return: An integer
		"""
		return randint(min_number, max_number)

	@staticmethod
	def generate_words(consonants: [] = None, vowel: [] = None) -> str:
		"""
		This static method generates a random word.
		:param consonants: A list of strings
		:param vowel: A list of strings
		:return: A string.
		"""

		# set default alphabet
		if consonants is None:
			consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

		if vowel is None:
			vowel = ["a", "e", "i", "o", "u"]

		# determine the word length
		length = Generator.__random_length(1, 9)

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
		This static method generates a random multilingual string.
		:return: A multilingual string.
		"""

		# determine the word length
		length = Generator.__random_length()

		# construct multilingual string
		string = String()
		string.state = State.GENERATED

		# add strings
		for language in ["Language A", "Language B", "Language C", "Language D"]:

			# store the result
			clause = ""

			# construct the word
			for _ in range(length):
				clause += Generator.generate_words() + " "

			clause = clause[:-1] + "."
			string.strings[language] = clause

		return string

	@staticmethod
	def __generate_nodes(layer: Layer, node_generation_range: {Layer: (int, int)} = None) -> [Node]:
		"""
		This static method generates a random library.
		:param layer: A layer
		:param node_generation_range: A dict with layers -> (range_min [int], range_max [int])
		:return: A node list
		"""

		# set default node generation range of every layer
		if node_generation_range is None:
			node_generation_range = {
				Layer.COLLECTION: (3, 14),
				Layer.BOOK: (3, 14),
				Layer.PART: (3, 14),
				Layer.CHAPTER: (3, 14),
				Layer.SECTION: (3, 14),
				Layer.PARAGRAPH: (3, 14),
				Layer.LINE: (3, 14)
			}
		node_generation_range[Layer.CLAUSE] = (0, 0)

		# break up if leaf node
		if Layer.CLAUSE == layer:
			node = Node(layer)
			node.title = Generator.generate_string()

		# construct nodes
		nodes = []
		for _ in range(Generator.__random_length(*node_generation_range[layer])):
			node = Node(layer)
			node.title = Generator.generate_string()
			node.children = Generator.__generate_nodes(layer.sublayer, node_generation_range)
			nodes.append([node])

		return nodes

	@staticmethod
	def generate_library() -> [Node]:
		"""
		This static method generates a random library.
		:return: A library.
		"""
		node_generation_range = {
			Layer.COLLECTION: (3, 5),
			Layer.BOOK: (3, 5),
			Layer.PART: (3, 5),
			Layer.CHAPTER: (3, 5),
			Layer.SECTION: (3, 5),
			Layer.PARAGRAPH: (3, 5),
			Layer.LINE: (3, 8)
		}
		return Generator.__generate_nodes(Layer.COLLECTION, node_generation_range)[0]
