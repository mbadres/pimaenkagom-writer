import unittest


class Testing(unittest.TestCase):

	def test_string(self):
		a = 'some'
		b = 'some'
		self.assertEqual(a, b)

	def test_int(self):
		a = 1
		b = 2
		self.assertNotEqual(a, b)


if __name__ == '__main__':
	unittest.main()
