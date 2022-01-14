from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


class Application(QApplication):
	"""
	This class represents the hole ui.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__([])
		self.setStyleSheet(open("resources/style.css", "r").read())
		self.window = QUiLoader().load("resources/form.ui")
		self.window.show()
		self.window.pushButton.clicked.connect(lambda: print("Aye"))
		self.window.pushButton_2.clicked.connect(lambda: print("Bye"))
