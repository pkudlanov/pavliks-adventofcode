import unittest
import a
import b


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

    def test_rinr_same(self):
        range_a = (1, 9)
        range_b = (1, 9)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, True)

    def test_rinr_end(self):
        range_a = (1, 9)
        range_b = (9, 18)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, False)

    def test_rinr_single(self):
        range_a = (6, 6)
        range_b = (6, 6)
        assignments = a.CleanupAssignments()

        result = assignments.range_inrange(range_a[0], range_a[1], range_b[0], range_b[1])

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()


class TestCampCleanupOverlapping(unittest.TestCase):

    def test_b(self):
        assignments = b.CleanupAssignments()
        result = assignments.result(f='test-input.txt')
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
