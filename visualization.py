import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data for a given stock for all months
def load_all_month_data(stock_name):
    all_month_data = []
    for month in range(1, 13):
        filename = f"{stock_name}_2023_{month:02d}.csv"
        df_month = pd.read_csv(filename)
        all_month_data.append(df_month)
    return all_month_data

# Function to plot comparative closing prices for all stocks for each month
def plot_comparative_closing_prices():
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 12))
    fig.suptitle("Comparative Closing Prices - Year 2023", fontsize=16)
    
    for month, ax in enumerate(axes.flat, start=1):
        for stock_name in ['AAPL', 'MSFT', 'GOOGL']:
            df_month = load_all_month_data(stock_name)[month-1]
            ax.plot(df_month['Close'], label=stock_name)
        ax.set_title(f"Month {month}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Function to plot comparative volume traded for all stocks for each month
def plot_comparative_volume_traded():
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 12))
    fig.suptitle("Comparative Volume Traded - Year 2023", fontsize=16)
    
    for month, ax in enumerate(axes.flat, start=1):
        for stock_name in ['AAPL', 'MSFT', 'GOOGL']:
            df_month = load_all_month_data(stock_name)[month-1]
            ax.plot(df_month['Volume'], label=stock_name)
        ax.set_title(f"Month {month}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Volume")
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Function to plot comparative daily returns distribution for all stocks for each month
def plot_comparative_daily_returns_distribution():
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 12))
    fig.suptitle("Comparative Daily Returns Distribution - Year 2023", fontsize=16)
    
    for month, ax in enumerate(axes.flat, start=1):
        for stock_name in ['AAPL', 'MSFT', 'GOOGL']:
            df_month = load_all_month_data(stock_name)[month-1]
            sns.histplot(df_month['Close'].pct_change(), kde=True, ax=ax, label=stock_name)
        ax.set_title(f"Month {month}")
        ax.set_xlabel("Daily Returns")
        ax.set_ylabel("Frequency")
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Function to plot comparative moving averages for all stocks for each month
def plot_comparative_moving_averages():
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 12))
    fig.suptitle("Comparative Moving Averages - Year 2023", fontsize=16)
    
    for month, ax in enumerate(axes.flat, start=1):
        for stock_name in ['AAPL', 'MSFT', 'GOOGL']:
            df_month = load_all_month_data(stock_name)[month-1]
            ax.plot(df_month['MA_50'], label=f"{stock_name}_MA_50")
            ax.plot(df_month['MA_200'], label=f"{stock_name}_MA_200")
        ax.set_title(f"Month {month}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

# Plot comparative visualizations for all metrics
plot_comparative_closing_prices()
plot_comparative_volume_traded()
plot_comparative_daily_returns_distribution()
plot_comparative_moving_averages()
