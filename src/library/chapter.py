from library.element import Element


class Chapter(Element):
	"""
	This class represents a chapter in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="chapter")
