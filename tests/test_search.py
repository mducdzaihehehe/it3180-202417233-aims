import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class SearchTests(unittest.TestCase):
    def test_title_substring(self):
        dvd = DigitalVideoDisc("The Lion King")
        self.assertEqual(search_by_title([dvd], "Lion"), [dvd])

    def test_case_insensitive(self):
        dvd = DigitalVideoDisc("The Lion King")
        self.assertEqual(search_by_title([dvd], "lion"), [dvd])
