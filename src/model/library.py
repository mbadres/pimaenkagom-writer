from model.multilingual_string import String
from util.generator import generate_id


class Element:
	"""
	This class represents an element in the library.
	"""

	def __init__(self, node_type=None):
		"""
		Constructor
		"""
		self.__id = generate_id()
		self.__title = String(empty=True)
		self.__titled = True
		self.__type = None
		self.__node_type = node_type
		self.__audible = True
		self.__visible = True
		self.__icon = ""
		self.__version = 1
		self.__children = [[]]

	def id(self):
		"""
		This method returns the id of the element.
		:return: An integer
		"""
		return self.__id

	def title(self):
		"""
		This method returns the title.
		:return: A multilingual string
		"""
		return self.__title

	def titled(self):
		"""
		This method returns true if the element is titled.
		:return: A boolean
		"""
		return self.__titled

	def type(self):
		"""
		This method returns the element type.
		:return: A string
		"""
		return self.__type

	def node_type(self):
		"""
		This method returns the element node type.
		:return: A string
		"""
		return self.__node_type

	def audible(self):
		"""
		This method returns true if the element is set audible.
		:return: A boolean
		"""
		return self.__audible

	def visible(self):
		"""
		This method returns true if the element is set visible.
		:return: A boolean
		"""
		return self.__visible

	def icon(self):
		"""
		This method returns the icon.
		:return: A string
		"""
		return self.__icon

	def version(self):
		"""
		This method returns the version.
		:return: An integer
		"""
		return self.__version

	def children(self):
		"""
		This method returns the children.
		:return: A list of lists
		"""
		return self.__children


class Clause(Element):
	"""
	This class represents a clause in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="clause")


class Line(Element):
	"""
	This class represents a line in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="line")


class Paragraph(Element):
	"""
	This class represents a paragraph in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="paragraph")


class Section(Element):
	"""
	This class represents a section in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="section")


class Chapter(Element):
	"""
	This class represents a chapter in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="chapter")


class Part(Element):
	"""
	This class represents a part in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="part")


class Book(Element):
	"""
	This class represents a book in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="book")


class Collection(Element):
	"""
	This class represents a collection in a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__(node_type="collection")


class Library:
	"""
	This class represents a library.
	"""

	def __init__(self):
		"""
		Constructor
		"""

		# store multilingual strings
		self.multilingual_strings = []

		# store library elements
		self.clauses = []
		self.lines = []
		self.paragraphs = []
		self.sections = []
		self.chapters = []
		self.parts = []
		self.books = []
		self.collections = []
