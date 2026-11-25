import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category

class CategoryTests(unittest.TestCase):
    def test_category(self):
        dvd = DigitalVideoDisc("Aladdin", "Animation")
        self.assertEqual(search_by_category([dvd], "animation"), [dvd])
