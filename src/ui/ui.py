from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


class UI(QApplication):
	"""
	This class represents the hole ui.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		super().__init__([])
		self.setStyleSheet(open("ui/style.css", "r").read())
		self.window = QUiLoader().load("ui/form.ui")
		self.window.show()
		self.window.pushButton.clicked.connect(lambda: print("Aye"))
		self.exec()
