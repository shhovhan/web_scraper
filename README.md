# Web Scraping

Project creates web scraper, to scrap web page like [Hacker News](https://news.ycombinator.com/) 
and handle the data in a specific way with storing usage info into a database

## Requirements

- Python (3.10)
- Beautifulsoup4
- Pytest

Tested on MacOS.

## Setup

First check if you have python installed by running command `python --version`. Most probably you have it already.
Otherwise, install corresponding version according to instructions of your OS.
For more details follow the [link](https://www.python.org/downloads/)

Next setup python environment:

- create virtual environment using `python -m venv <path_to_env>` or use instruction [here](https://docs.python.org/3/library/venv.html)
- activate virtual environment: `source <path_to_venv>/bin/activate`
- clone code or download zip anywhere in your local machine
- go to **web_crawler** project and install requirements: `pip install -r requirements.txt`

## Usage

From `web_crawler` directory run `main.py`

```
python main.py
```

## Database

`SQLite` is used for storing data in a database. For that, a special **storage** module has created,
which contains **UsageDataStorage** class. It handles db connection with SQLite, creating a table and
adding data in it.

**SQLite** is light, no need for any special installation or setup for connecting and working with database.

## Running Tests

Project contains unit test written in unittest library. You will find them in `tests` folder.

`Pytest` is used to run all tests automatically.

To do it, just run the following command and it will automatically run all tests under the folder.

```
pytest
```


==================================

**Author:** Shushanik Hovhannesyan

**Email:** shushhovhannisyan@gmail.com