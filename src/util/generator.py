import uuid


def generate_id():
	"""
	This function generates a random id.
	:return: A 64-bit integer
	"""
	maxint64 = (1 << 64) - 1
	randint128 = uuid.uuid4().int
	return maxint64 & randint128
