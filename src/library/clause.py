from library.element import Element


class Clause(Element):
	"""
	This class represents a clause in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="clause")
