import re


class EntryFilter:
    def __init__(self, entries):
        self.entries = entries

    @staticmethod
    def _count_words(title):
        # Remove any symbols and count words by splitting with spaces
        return len(re.findall(r'\b\w+\b', title))

    def filter_more_than_five_words(self):
        filtered = [entry for entry in self.entries if self._count_words(entry['title']) > 5]
        return sorted(filtered, key=lambda x: x['comments'], reverse=True)

    def filter_five_or_fewer_words(self):
        filtered = [entry for entry in self.entries if self._count_words(entry['title']) <= 5]
        return sorted(filtered, key=lambda x: x['points'], reverse=True)