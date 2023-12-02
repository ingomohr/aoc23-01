""" Test for number_adapter """
import unittest
import aoc23_01.number_adapter as a


class TestNumberAdapter(unittest.TestCase):
    """ . """

    def test_adapt_to_number(self):
        """ Tests adapt_to_number """

        self.assertEqual(a.adapt_to_number('42'), 42)


if __name__ == '__main__':
    unittest.main()
