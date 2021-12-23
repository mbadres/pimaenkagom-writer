class Observable:
	"""
	This class represents an observable.
	"""

	def __init__(self):
		"""
		Constructor
		"""
		self.__observers = []

	def attach(self, observer):
		"""
		This method registers the observer at the observable.
		:param observer: An observer
		"""
		self.__observers.append(observer)

	def detach(self, observer):
		"""
		This method sign the observer out.
		:param observer: The observer
		"""
		self.__observers.remove(observer)

	def notify(self, *args, **kwargs):
		"""
		This method notify all observers.
		:param args: mics
		:param kwargs: mics
		"""
		for observer in self.__observers:
			observer.update(self, *args, **kwargs)


class Observer:
	"""
	This class represents an observer.
	"""

	def __init__(self):
		"""
		Constructor
		"""

	def observe(self, observable):
		"""
		This method registers the observer to the observable
		:param observable: The observable
		"""
		observable.attach(self)

	def stop_observing(self, observable):
		"""
		This method signs off the observer from the observable
		:param observable: The observable
		"""
		observable.detach(self)

	def update(self, observable, *args, **kwargs):
		"""
		This method updates the observer.
		It has to be overridden after inheritance.
		:param observable: An observable
		:param args:
		:param kwargs:
		"""
		print("Got", args, kwargs, "From", observable)
