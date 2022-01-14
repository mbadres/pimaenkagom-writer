from library.element import Element


class Line(Element):
	"""
	This class represents a line in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="line")
