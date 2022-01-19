from library.element import Element
from library.node import Node


class Line(Element):
	"""
	This class represents a line in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.Line)
