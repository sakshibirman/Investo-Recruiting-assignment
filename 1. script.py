import sqlite3
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
import unittest
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

# Function to ingest OHLC data for a given stock
def ingest_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

# Function to clean the data
def clean_data(df):
    df = df.dropna().copy()  # Drop rows with NaN values
    z_scores = ((df - df.mean()) / df.std()).abs()
    df = df[(z_scores < 3).all(axis=1)]  # Keep only rows where z-score < 3
    return df

# Function to calculate technical indicators
def calculate_technical_indicators(df):
    # Calculate moving averages (e.g., 50-day and 200-day)
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['MA_200'] = df['Close'].rolling(window=200).mean()
    # Calculate Bollinger Bands
    window = 20
    df['MA'] = df['Close'].rolling(window=window).mean()
    df['std'] = df['Close'].rolling(window=window).std()
    df['Upper_BB'] = df['MA'] + 2 * df['std']
    df['Lower_BB'] = df['MA'] - 2 * df['std']
    # Calculate RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

# Function to engineer additional features
def engineer_features(df):
    df['Volatility'] = df['Close'].pct_change().rolling(window=20).std() * np.sqrt(252)
    df['Price_vs_MA50'] = df['Close'] - df['MA_50']
    return df

# Function to store data in a SQLite database partitioned by year and month
def store_partitioned_data(df, database_name, table_name):
    engine = create_engine(f'sqlite:///{database_name}.db')
    for year, month in zip(df.index.year, df.index.month):
        partition_name = f"{table_name}_{year}_{month:02d}"
        df_month = df[(df.index.year == year) & (df.index.month == month)]
        df_month.to_sql(partition_name, engine, index=False, if_exists='replace')

# Function to fetch data from a specific table and return it as a DataFrame
def fetch_table_data_as_dataframe(table_name):
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    return df

# Function to export data from a specific table as a CSV file
def export_table_as_csv(table_name, csv_filename):
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    df.to_csv(csv_filename, index=False)

# Function to validate the data pipeline through unit tests
class TestDataPipeline(unittest.TestCase):
    def test_data_ingestion(self):
        # Test data ingestion for a sample stock ticker
        df = ingest_stock_data('AAPL', '2023-01-01', '2024-01-01')
        self.assertIsNotNone(df)
        self.assertTrue(len(df) > 0)

    def test_data_cleaning(self):
        # Test data cleaning for a sample DataFrame with NaN values
        sample_data = {'Open': [100, None, 105, 110],
                       'High': [102, None, 108, 112],
                       'Low': [98, None, 103, 108],
                       'Close': [101, None, 106, 109]}
        df = pd.DataFrame(sample_data)
        cleaned_df = clean_data(df)
        self.assertEqual(len(cleaned_df), 3)
        self.assertNotIn(None, cleaned_df.values)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main(argv=[''], exit=False)
    
    # Connect to the SQLite database file
    conn = sqlite3.connect('stock_data.db')
    
    # Example usage
    tickers = ['AAPL', 'MSFT', 'GOOGL']  # Sample list of stock tickers
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    
    for ticker in tickers:
        # Ingest data
        df = ingest_stock_data(ticker, start_date, end_date)
        
        # Clean data
        df_cleaned = clean_data(df)
        
        # Calculate technical indicators
        df_transformed = calculate_technical_indicators(df_cleaned)
        
        # Engineer additional features
        df_features = engineer_features(df_transformed)
        
        # Store data in SQLite database partitioned by year and month
        store_partitioned_data(df_features, database_name='stock_data', table_name=ticker)

    # Fetch and display data from all tables
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        df = fetch_table_data_as_dataframe(table_name)
        print(f"Data from table '{table_name}':")
        print(df)
        print("\n")
        
        # Export table as CSV
        csv_filename = f"{table_name}.csv"
        export_table_as_csv(table_name, csv_filename)
        print(f"Exported '{table_name}' table to '{csv_filename}'")
    
    # Close the connection
    cursor.close()
    conn.close()
