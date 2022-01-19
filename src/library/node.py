from enum import Enum


class Node(Enum):
	"""
	This class enumerates the type of library node.
	"""

	# Library = 0
	Collection = 1
	Book = 2
	Part = 3
	Chapter = 4
	Section = 5
	Paragraph = 6
	Line = 7
	Clause = 8
