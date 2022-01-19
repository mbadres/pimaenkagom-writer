from library.element import Element
from library.node import Node


class Book(Element):
	"""
	This class represents a book in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.BOOK)
