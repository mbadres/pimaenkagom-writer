from enum import Enum


class Node(Enum):
	"""
	This class enumerates the type of library node.
	"""

	# LIBRARY = 0
	COLLECTION = 1
	BOOK = 2
	PART = 3
	CHAPTER = 4
	SECTION = 5
	PARAGRAPH = 6
	LINE = 7
	CLAUSE = 8
