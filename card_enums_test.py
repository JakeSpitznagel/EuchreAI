import unittest

from card_enums import Suit, Value


class ValueTests(unittest.TestCase):
    def test_comparision(self):
        self.assertLess(Value.nine, Value.ten)
        self.assertGreater(Value.ace, Value.king)
