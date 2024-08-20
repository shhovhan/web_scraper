from scraper.scraper import HackerNewsScraper
from scraper.filters import EntryFilter
from scraper.storage import UsageDataStorage


def main():
    """
    Main function that combines the scraping, filtering, and storage of Hacker News entries.

    This function performs the following operations:
    1. Initializes a `HackerNewsScraper` to fetch entries from Hacker News.
    2. Filters the fetched entries using the `EntryFilter` class.
    3. Stores the usage data in an SQLite database using the `UsageDataStorage` class.
    4. Filters the entries into two categories:
       - Entries with more than five words in the title.
       - Entries with five or fewer words in the title.
    5. Inserts the count of filtered entries into the database.
    6. Fetches and returns all usage data stored in the database.

    Returns:
    --------
    tuple:
        A tuple containing the following:
        - more_than_five_words (list):
            Filtered entries with more than five words in the title.
        - five_or_fewer_words (list):
            Filtered entries with five or fewer words in the title.
        - db_usage_data (list of tuple):
            All records from the 'usage_data' table in the database,
           where each record is represented as a tuple
           (id, timestamp, filter_type, entries_count).
    """
    scraper = HackerNewsScraper()
    entries = scraper.fetch()
    entry_filter = EntryFilter(entries)
    db = UsageDataStorage()

    # Filter entries
    more_than_five_words = entry_filter.filter_more_than_five_words()
    five_or_fewer_words = entry_filter.filter_five_or_fewer_words()

    # Add usage data in database
    db.insert_usage_data('more_than_five', len(more_than_five_words))
    db.insert_usage_data('five_or_fewer', len(five_or_fewer_words))

    db_usage_data = db.fetch_usage_data()
    return more_than_five_words, five_or_fewer_words, db_usage_data


if __name__ == '__main__':
    more_than_five, five_or_fewer, usage_data = main()

    print('Entries with more than 5 words in title: ', more_than_five)
    print('Entries with fewer or 5 words in title: ', five_or_fewer)
    print('Usage data from usage_data database: ', usage_data)
