import unittest
import a
import b


class TestRucksackReorganization(unittest.TestCase):

    def test_a(self):
        pack = a.PackOrganizer(f='test-input.txt')
        result = pack.result()
        self.assertEqual(result, 157)

    def test_b(self):
        pack = b.PackOrganizer(f='test-input.txt')
        result = pack.result()
        self.assertEqual(result, 70)


if __name__ == '__main__':
    unittest.main()
