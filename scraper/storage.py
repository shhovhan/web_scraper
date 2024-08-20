import sqlite3
from datetime import datetime
from config.constants import DB_NAME


class UsageDataStorage:
    """
        A class to handle the storage and retrieval of usage data.
    """
    def __init__(self, db_name=DB_NAME):
        """
        Initializes the UsageDataStorage with a connection to the database
        and creates the table 'usage_data'.

        Parameters:
        -----------
        db_name : str, optional
            The name of the SQLite database file (default is 'usage_data.db').
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Creates the 'usage_data' table in the database if it does not exist.

        The table contains the following columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - timestamp: TEXT
        - filter_type: TEXT
        - entries_count: INTEGER
        """
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS usage_data (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 timestamp TEXT,
                                 filter_type TEXT,
                                 entries_count INTEGER)''')

    def insert_usage_data(self, filter_type, entries_count):
        """
        Inserts a new record into the 'usage_data' table.

        Parameters:
        -----------
        filter_type : str
            The type of filter applied.
        entries_count : int
            The number of entries returned after applying the filter.
        """
        with self.conn:
            self.conn.execute('''INSERT INTO usage_data 
                                (timestamp, filter_type, entries_count) 
                                VALUES (?, ?, ?)''',
                              (datetime.now(), filter_type, entries_count))

    def fetch_usage_data(self):
        """
        Fetches all records from 'usage_data' table.

        Returns:
        --------
        list of tuple
            A list containing all the records from the 'usage_data' table.
            (id, timestamp, filter_type, entries_count).
        """
        with self.conn:
            return self.conn.execute('SELECT * FROM usage_data').fetchall()
