from scraper.scraper import HackerNewsScraper
from scraper.filters import EntryFilter


def main():
    scraper = HackerNewsScraper()
    entries = scraper.fetch()
    entry_filter = EntryFilter(entries)

    # Filter entries
    more_than_five = entry_filter.filter_more_than_five_words()
    five_or_fewer = entry_filter.filter_five_or_fewer_words()

    return more_than_five, five_or_fewer


if __name__ == '__main__':
    more_than_five, five_or_fewer = main()
    print(more_than_five, five_or_fewer)