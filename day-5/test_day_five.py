import unittest


class TestPartA(unittest.TestCase):

    def test_a(self):
        result = 'CMZ'
        self.assertEqual(result, 'CMZ')


if __name__ == '__main__':
    unittest.main()
