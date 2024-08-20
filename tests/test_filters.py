import unittest

from scraper.filters import EntryFilter


class TestEntryFilters(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = [
            {
                'title': 'Entry with more than five words in the title',
                'points': 100,
                'comments': 10
            },
            {
                'title': 'Another entry with more than five word in the title',
                'points': 100,
                'comments': 10
            },
            {
                'title': 'Short title',
                'points': 200,
                'comments': 5
            }
        ]
        self.entry_filter = EntryFilter(self.entries)

    def test_filter_more_than_five_words(self):
        filtered = self.entry_filter.filter_more_than_five_words()
        self.assertEqual(len(filtered), 2)

    def test_filter_five_or_fewer_words(self):
        filtered = self.entry_filter.filter_five_or_fewer_words()
        self.assertEqual(len(filtered), 1)
