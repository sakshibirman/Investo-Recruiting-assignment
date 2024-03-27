# Investo-Recruiting-assignment
## Assignment I was given for Selection round by Investo Team.

### Scenario: 
You are a data engineer for a hedge fund that trades based on technical analysis. Your team needs a robust pipeline to process and analyze large volumes of historical stock data efficiently. You are tasked with building a data pipeline that cleans, transforms, and aggregates Open, High, Low, and Close (OHLC) data for further analysis and model development.

### Data Source:
• Your company receives daily OHLC data feeds for multiple stocks in various formats (e.g., CSV, JSON).
• Eg: Yahoo Finance/yfinance - try 5-10 equities as a sample dataset

### Tasks:

1. Data Ingestion:
• Develop a script that can ingest OHLC data feeds from various sources and formats.
• Validate the data integrity (e.g., check for missing values, outliers, data type consistency).
• Standardize the data format to a common structure (e.g., pandas DataFrame).
2. Data Cleaning:
• Identify and handle missing values (e.g., imputation, removal).
• Detect and correct outliers using statistical methods or domain knowledge.
• Address any inconsistencies in timestamps or date formats.
3. Data Transformation:
• Calculate technical indicators based on OHLC data (e.g., moving averages, Bollinger Bands, Relative Strength Index).
• Apply feature engineering techniques to create new features relevant for your trading strategy (e.g., volatility measures, price patterns).
• Resample the data based on desired frequencies (e.g., daily to hourly).
4. Data Validation:
• Implement unit tests to ensure the pipeline's functionality and data integrity.
• Monitor the pipeline for errors and data quality issues.
5. Data Storage:
• Use a simple DB to store this (such as Sqlite, Mysql etc)
• Partition the data by year, month, or another relevant category for efficient querying.
• Optimize the data format for fast retrieval and analysis (e.g., columnar format).

Bonus:
• Implement data compression techniques to reduce storage costs.
• Integrate the pipeline with a visualization tool to explore the data interactively.
• Develop data quality checks and alerts to proactively identify and address issues.

Deliverables:
• A well-documented Python script implementing the data pipeline.
• Example output showing cleaned and transformed data for a specific period.
• (Optional) Visualization or report showcasing key insights from the processed data.

Technologies:
• Python libraries: pandas, numpy, Dask (for large datasets), data validation libraries (e.g., pytest)
• Cloud storage or data warehouse (e.g., AWS S3, Google Cloud Storage, Snowflake) (optional)
• Visualization tools (e.g., Tableau, Power BI) (optional)
