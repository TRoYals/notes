---
title: sqlalcemy best pratice
date: 2023-08-15 10:37
article: false
tags: 
---
```python
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, insert


class DatabaseConnector:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Get database connection parameters from environment variables
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")

        # Initialize the SQLAlchemy engine and connection attributes
        self.engine = None
        self.conn = None

    def connect(self):
        try:
            # Create the database URI using SQLAlchemy format
            db_uri = f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

            # Connect to the database using SQLAlchemy
            self.engine = create_engine(db_uri)
            self.conn = self.engine.connect()

            print("Database connection successful.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def fetch_data(self,query):
        try:
            # Fetch data from the database using pandas and the SQLAlchemy connection
            df = pd.read_sql(query, self.conn)
            print(df)
        except Exception as e:
            print(f"Error fetching data: {e}")

    def insert_data(self, table_name, data_dict):
        try:
            # Get the MetaData object
            metadata = MetaData()

            # Reflect the table structure directly from the engine
            table = Table(table_name, metadata, autoload_with=self.engine)

            # Create an insert statement
            stmt = insert(table).values(data_dict)

            # Execute the insert statement
            self.conn.execute(stmt)
            self.conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def close(self):
        try:
            # Close the SQLAlchemy connection
            if self.conn:
                self.conn.close()
            print("Database connection closed.")
        except Exception as e:
            print(f"Error closing the database connection: {e}")



def main():
    db_connector = DatabaseConnector()
    db_connector.connect()

    # Fetch data
    db_connector.fetch_data("SELECT * FROM maimai.maimai_DB")

    # Insert data
    new_data = {"BPM": 100,"song_name": "test"}
    db_connector.insert_data("maimai_DB", new_data)
    db_connector.fetch_data("SELECT * FROM maimai.maimai_DB")

    db_connector.close()


if __name__ == "__main__":
    main()
```
