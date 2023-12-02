""" Test for number_adapter """
import unittest
import number_adapter as a


class TestNumberAdapter(unittest.TestCase):
    """ . """

    def test_adapt_to_number(self):
        """ Tests adapt_to_number """

        self.assertEqual(a.adapt_to_number('42'), 42)
        self.assertEqual(a.adapt_to_number('a4a2a'), 42)


if __name__ == '__main__':
    unittest.main()
