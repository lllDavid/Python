import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Let's assume you already have historical cryptocurrency data in a CSV or fetched from an API
# For this example, I will simulate loading a CSV with data for 3 cryptocurrencies (Bitcoin, Ethereum, and Litecoin).

# Simulated data (in reality, you'd load this from an API or a file)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Bitcoin': np.random.normal(40000, 5000, 100),  # Randomized Bitcoin prices with some fluctuation
    'Ethereum': np.random.normal(3000, 200, 100),   # Ethereum prices
    'Litecoin': np.random.normal(150, 20, 100)      # Litecoin prices
}

# Creating the DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 1. Data Cleaning: Handling missing values (if any)
df = df.fillna(method='ffill')  # Forward fill to handle missing data

# 2. Calculate Moving Averages (30-day and 90-day)
df['Bitcoin_MA30'] = df['Bitcoin'].rolling(window=30).mean()
df['Ethereum_MA30'] = df['Ethereum'].rolling(window=30).mean()
df['Litecoin_MA30'] = df['Litecoin'].rolling(window=30).mean()

df['Bitcoin_MA90'] = df['Bitcoin'].rolling(window=90).mean()
df['Ethereum_MA90'] = df['Ethereum'].rolling(window=90).mean()
df['Litecoin_MA90'] = df['Litecoin'].rolling(window=90).mean()

# 3. Calculate Daily Returns (percentage change)
df['Bitcoin_Returns'] = df['Bitcoin'].pct_change()
df['Ethereum_Returns'] = df['Ethereum'].pct_change()
df['Litecoin_Returns'] = df['Litecoin'].pct_change()

# 4. Calculate Volatility (Standard Deviation of Returns)
volatility = {
    'Bitcoin_Volatility': df['Bitcoin_Returns'].std() * np.sqrt(365),  # Annualized volatility
    'Ethereum_Volatility': df['Ethereum_Returns'].std() * np.sqrt(365),
    'Litecoin_Volatility': df['Litecoin_Returns'].std() * np.sqrt(365)
}

# 5. Calculate Correlation between Cryptocurrencies
correlation_matrix = df[['Bitcoin', 'Ethereum', 'Litecoin']].pct_change().corr()

# 6. Plotting the prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Bitcoin'], label='Bitcoin Price', color='orange')
plt.plot(df.index, df['Bitcoin_MA30'], label='Bitcoin 30-Day MA', linestyle='--', color='blue')
plt.plot(df.index, df['Ethereum'], label='Ethereum Price', color='green')
plt.plot(df.index, df['Ethereum_MA30'], label='Ethereum 30-Day MA', linestyle='--', color='red')
plt.plot(df.index, df['Litecoin'], label='Litecoin Price', color='purple')
plt.plot(df.index, df['Litecoin_MA30'], label='Litecoin 30-Day MA', linestyle='--', color='brown')

plt.title('Cryptocurrency Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Output the volatility and correlation matrix
print("Cryptocurrency Volatility (Annualized):")
print(volatility)

print("\nCryptocurrency Correlation Matrix (Daily Returns):")
print(correlation_matrix)

