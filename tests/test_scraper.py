import unittest

from scraper.scraper import HackerNewsScraper


class TestHackerNews(unittest.TestCase):
    def setUp(self):
        self.scraper = HackerNewsScraper()

    def test_entry_count(self):
        entries = self.scraper.fetch()
        self.assertEqual(len(entries), 30)


