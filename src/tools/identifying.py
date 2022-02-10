import uuid


"""
This type represents the ID.
"""
ID = str


def generate_id() -> ID:
	"""
	This static method generates a random id.
	:return: A string
	"""
	# maxint64 = (1 << 64) - 1
	# randint128 = uuid.uuid4().int
	# return maxint64 & randint128
	return str(uuid.uuid4())
