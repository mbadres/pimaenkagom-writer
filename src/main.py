import sys

from model.master import Master
from ui.application import Application

if __name__ == '__main__':

	# load model
	maestro = Master()

	# load the ui at last
	app = Application()
	code = app.exec()
	sys.exit(code)
