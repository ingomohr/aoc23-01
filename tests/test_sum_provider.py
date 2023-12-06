""" Test for sum_provider """
import unittest
import src.sum_provider as provider


class TestSumProvider(unittest.TestCase):
    """ TestCase impl for sum_provider """

    def test_sum_provider(self):
        """ Tests example input with its expected result """

        self.assertEqual(provider.get_sum("tests/sample_values.txt"), 142)


if __name__ == '__main__':
    unittest.main()
