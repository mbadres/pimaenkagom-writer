from library.element import Element
from library.node import Node


class Collection(Element):
	"""
	This class represents a collection in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.Collection)
