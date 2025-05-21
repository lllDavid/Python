import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Bitcoin': np.random.normal(40000, 5000, 100),
    'Ethereum': np.random.normal(3000, 200, 100),
    'Litecoin': np.random.normal(150, 20, 100)
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df = df.fillna(method='ffill')

df['Bitcoin_MA30'] = df['Bitcoin'].rolling(window=30).mean()
df['Ethereum_MA30'] = df['Ethereum'].rolling(window=30).mean()
df['Litecoin_MA30'] = df['Litecoin'].rolling(window=30).mean()

df['Bitcoin_MA90'] = df['Bitcoin'].rolling(window=90).mean()
df['Ethereum_MA90'] = df['Ethereum'].rolling(window=90).mean()
df['Litecoin_MA90'] = df['Litecoin'].rolling(window=90).mean()

df['Bitcoin_Returns'] = df['Bitcoin'].pct_change()
df['Ethereum_Returns'] = df['Ethereum'].pct_change()
df['Litecoin_Returns'] = df['Litecoin'].pct_change()

volatility = {
    'Bitcoin_Volatility': df['Bitcoin_Returns'].std() * np.sqrt(365),
    'Ethereum_Volatility': df['Ethereum_Returns'].std() * np.sqrt(365),
    'Litecoin_Volatility': df['Litecoin_Returns'].std() * np.sqrt(365)
}

correlation_matrix = df[['Bitcoin', 'Ethereum', 'Litecoin']].pct_change().corr()

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

print("Cryptocurrency Volatility (Annualized):")
print(volatility)

print("\nCryptocurrency Correlation Matrix (Daily Returns):")
print(correlation_matrix)
