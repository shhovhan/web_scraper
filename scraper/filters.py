import re


class EntryFilter:
    """
    A class to filter and sort Hacker News entries based on the number of words in their titles.
    """
    def __init__(self, entries):
        """
        Initializes the EntryFilter with a list of entries.

        Parameters:
        -----------
        entries : list of dict
            The list of Hacker News entries to be filtered.
        """
        self.entries = entries

    @staticmethod
    def _count_words(title):
        """
        Counts the number of words in a title, ignoring symbols.

        Parameters:
        -----------
        title : str
            The title of the entry.

        Returns:
        --------
        int
            The number of words in the title.
        """
        return len(re.findall(r'\b\w+\b', title))

    def filter_more_than_five_words(self):
        """
        Filters entries with more than five words in their titles,
        sorts them by the number of comments.

        Returns:
        --------
        list of dict
            A list of filtered entries sorted by the number of comments in descending order.
        """
        filtered = [entry for entry in self.entries if self._count_words(entry['title']) > 5]
        return sorted(filtered, key=lambda x: x['comments'], reverse=True)

    def filter_five_or_fewer_words(self):
        """
        Filters entries with five or fewer words in their titles,
        sorts them by the number of points.

        Returns:
        --------
        list of dict
            A list of filtered entries sorted by the number of points in descending order.
        """
        filtered = [entry for entry in self.entries if self._count_words(entry['title']) <= 5]
        return sorted(filtered, key=lambda x: x['points'], reverse=True)