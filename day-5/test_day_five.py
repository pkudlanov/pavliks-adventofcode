import unittest
import a


class TestPartA(unittest.TestCase):

    def test_stack_crate(self):
        supplies = a.Supplies()
        supplies.stack_crate(stack='5', crate='Y')
        supplies.stack_crate(stack='5', crate='G')
        supplies.stack_crate(stack='2', crate='P')

        result = supplies.stacks

        self.assertEqual(result, {'2': ['P'], '5': ['G', 'Y']})

    def test_build_stacks(self):
        supplies = a.Supplies()
        supplies.build_stacks(f='test-input.txt')

        result = supplies.stacks

        self.assertEqual(result, {'1': ['Z', 'N'], '2': ['M', 'C', 'D'], '3': ['P']})

    def test_move_crates(self):
        supplies = a.Supplies()
        supplies.build_stacks(f='test-input.txt')

        supplies.move_crates(from_stack='2', to_stack='3', crates_amount=2)

        result = supplies.stacks

        self.assertEqual(result, {'1': ['Z', 'N'], '2': ['M'], '3': ['P', 'D', 'C']})

    def test_last_crates(self):
        supplies = a.Supplies()
        supplies.build_stacks(f='test-input.txt')

        result = supplies.last_crates()

        self.assertEqual(result, 'NDP')

    def test_run_procedure(self):
        supplies = a.Supplies()
        supplies.build_stacks(f='test-input.txt')
        supplies.run_procedure(f='test-input.txt')

        result = supplies.last_crates()

        self.assertEqual(result, 'CMZ')


if __name__ == '__main__':
    unittest.main()
