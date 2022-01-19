from library.element import Element
from library.node import Node


class Paragraph(Element):
	"""
	This class represents a paragraph in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type=Node.PARAGRAPH)
