""" Test for sum_provider """
import unittest
import aoc23_01.sum_provider as provider


class TestSumProvider(unittest.TestCase):
    """ . """

    def test_sum_provider(self):
        """ Tests example input with its expected result """

        self.assertEqual(provider.get_sum("sample_values.txt"), 42)


if __name__ == '__main__':
    unittest.main()
