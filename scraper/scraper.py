import requests
from bs4 import BeautifulSoup
from config.constants import URL, LIMIT


class WebScraper:
    def __init__(self, url):
        """
        Initializes the WebScraper with the provided URL
        and an empty list of entries.

        Parameters:
        -----------
        url : str
            The URL of the page to scrape.
        """
        self.url = url
        self.entries = []

    def fetch(self):
        pass


class HackerNewsScraper(WebScraper):
    """
    A web scraper for extracting the top entries from Hacker News.

    """
    def __init__(self, url=URL):
        super().__init__(url)

    def fetch(self):
        """
        Fetches the first `LIMIT` entries from Hacker News,
        extracting the rank, title, points, and comments.

        This method sends an HTTP GET request to the specified Hacker News URL,
        parses the HTML content using BeautifulSoup and extracts the relevant
        details for each of the top entries on the page.

        The extracted details include:
        - `number`: The rank of the entry on the page.
        - `title`: The title of the entry.
        - `points`: The number of points the entry has received.
        - `comments`: The number of comments the entry has received.

        Returns:
        --------
        list
            A list of dictionaries,
            where each dictionary contains the details of a Hacker News entry.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('tr', class_='athing')[:LIMIT]

        for item in items:
            number = int(item.find('span', class_='rank').text.strip('.'))
            title = item.find('span', class_='titleline').select_one('a').text
            subtext = item.find_next_sibling('tr').find('td', class_='subtext')

            points = subtext.find('span', class_='score')
            points = int(points.get_text().split()[0]) if points else 0

            comments = subtext.find_all('a')[-1].get_text()
            comments = int(comments.split()[0]) if 'comment' in comments else 0

            self.entries.append({
                'number': number,
                'title': title,
                'points': points,
                'comments': comments
            })

        return self.entries
