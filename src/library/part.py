from library.element import Element
from library.node import Node


class Part(Element):
	"""
	This class represents a part in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.PART)
