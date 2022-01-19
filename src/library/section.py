from library.element import Element
from library.node import Node


class Section(Element):
	"""
	This class represents a section in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.Section)
