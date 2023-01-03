"""金額テスト
"""
import unittest as ut
from moneys import dollar


class MoneyTest(ut.TestCase):
    """Moneyクラスのテスト

    Args:
        ut (_type_): _description_
    """
    def test_multiplication(self):
        """テスト
        """
        five = dollar.Dollar(5)
        product = five.times(2)
        five.times(2)
        self.assertEqual(10, product.amount, "amount expected 10")

        product = five.times(3)
        self.assertEqual(15, product.amount, "amount expected 30")

    def test_equality(self):
        """同一性テスト
        """
        self.assertTrue(dollar.Dollar(5) == dollar.Dollar(5), "$5 == $5")
        self.assertFalse(dollar.Dollar(5) == dollar.Dollar(6), "$5 != $6")
