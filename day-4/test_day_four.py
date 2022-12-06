import unittest
import a


class TestCampCleanup(unittest.TestCase):

    def test_a(self):
        pack = a.CleanupAssignments(f='test-input.txt')
        result = pack.result()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
