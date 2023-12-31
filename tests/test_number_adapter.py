""" Test for number_adapter """
import unittest
import src.number_adapter as adapter


class TestNumberAdapter(unittest.TestCase):
    """ TestCase impl for number_adapter """

    def test_adapt_to_number(self):
        """ Tests adapt_to_number """

        self.assertEqual(adapter.adapt_to_number('42'), 42)
        self.assertEqual(adapter.adapt_to_number('a4a3'), 43)
        self.assertEqual(adapter.adapt_to_number('4a5g'), 45)
        self.assertEqual(adapter.adapt_to_number('4a2hj_7g'), 47)

    def test_adapt_to_number_samples(self):
        """ Tests adapt_to_number with samples from the problem description """

        self.assertEqual(adapter.adapt_to_number('1abc2'), 12)
        self.assertEqual(adapter.adapt_to_number('pqr3stu8vwx'), 38)
        self.assertEqual(adapter.adapt_to_number('a1b2c3d4e5f'), 15)
        self.assertEqual(adapter.adapt_to_number('treb7uchet'), 77)


if __name__ == '__main__':
    unittest.main()
