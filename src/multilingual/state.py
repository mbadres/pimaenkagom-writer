from enum import Enum


class State(Enum):
	"""
	This class enumerates the states of a multilingual string.
	"""

	OK = 0
	INCOMPLETE = 1
	DEFICIENT = 3
	GENERATED = 4
