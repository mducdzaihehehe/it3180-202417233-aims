import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class SortTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", cost=1))
        self.cart.add_dvd(DigitalVideoDisc("A", cost=5))

    def test_sort_title(self):
        self.assertEqual([d.title for d in self.cart.sort_by_title()], ["A", "B"])

    def test_sort_cost(self):
        self.assertEqual([d.cost for d in self.cart.sort_by_cost()], [1, 5])
