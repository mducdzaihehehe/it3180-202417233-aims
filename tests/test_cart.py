import unittest
from contextlib import redirect_stdout
from io import StringIO
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class CartTests(unittest.TestCase):
    def test_capacity(self):
        cart = Cart()
        with redirect_stdout(StringIO()):
            for number in range(20):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(number))))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("extra")))
        self.assertEqual(len(cart.items), 20)

    def test_remove_disc(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Sample", cost=12)
        cart.add_dvd(dvd)
        self.assertEqual(cart.total_cost(), 12)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertEqual(cart.total_cost(), 0)


    def test_discounted_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Example", cost=100))
        self.assertEqual(cart.total_cost_with_discount(20), 80)

    def test_invalid_discount(self):
        for value in (-1, 150):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Cart().total_cost_with_discount(value)
