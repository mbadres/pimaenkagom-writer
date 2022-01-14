from library.element import Element


class Collection(Element):
	"""
	This class represents a collection in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="collection")
