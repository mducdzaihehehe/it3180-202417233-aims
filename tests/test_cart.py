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
