import unittest
import a


class TestCampCleanup(unittest.TestCase):

    def test_a(self):
        assignments = a.CleanupAssignments()
        result = assignments.result(f='test-input.txt')
        self.assertEqual(result, 2)

    def test_rinr_in(self):
        range_a = (1, 9)
        range_b = (2, 6)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, True)

    def test_rinr_out(self):
        range_a = (1, 9)
        range_b = (12, 18)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, False)

    def test_rinr_partial(self):
        range_a = (1, 9)
        range_b = (5, 18)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
