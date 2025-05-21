import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 100000
user_ids = np.random.randint(1, 10000, size=n)
categories = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Books'], size=n)
amounts = np.random.gamma(2., 50., size=n)
payment_methods = np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], size=n)
locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], size=n)
dates = pd.date_range('2023-01-01', periods=n, freq='T')

df = pd.DataFrame({
    'Transaction Date': dates,
    'User ID': user_ids,
    'Product Category': categories,
    'Amount': amounts,
    'Payment Method': payment_methods,
    'Location': locations
})

df = df.drop_duplicates()

df['Amount'] = df['Amount'].fillna(df['Amount'].mean())
df['Location'] = df['Location'].fillna('Unknown')

df = pd.get_dummies(df, columns=['Product Category', 'Payment Method', 'Location'], drop_first=True)

df.set_index('Transaction Date', inplace=True)
daily_transactions = df.resample('D').agg({'Amount': 'sum', 'User ID': 'nunique'})

plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(daily_transactions.index, daily_transactions['Amount'], label='Total Amount', color='b')
plt.title('Total Transaction Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Amount (USD)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(daily_transactions.index, daily_transactions['User ID'], label='Unique Users', color='r')
plt.title('Unique Users Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Unique Users')
plt.legend()

plt.tight_layout()
plt.show()

grouped_data = df.groupby(['Product Category_Electronics', 'Payment Method_Credit Card']).agg(
    total_amount=('Amount', 'sum'),
    transaction_count=('Amount', 'size'),
    average_amount=('Amount', 'mean')
).reset_index()

df['30_day_moving_avg'] = df['Amount'].rolling(window=30).mean()

df['30_day_moving_avg'].plot(figsize=(14, 6), title='30-Day Moving Average of Transaction Amounts', color='g')
plt.xlabel('Date')
plt.ylabel('Amount (USD)')
plt.show()

pivot_table = pd.pivot_table(df, values='Amount', 
                             index=['Location_Houston', 'Location_Miami'], 
                             columns=['Product Category_Books', 'Product Category_Electronics'],
                             aggfunc=np.sum, 
                             fill_value=0)

print(pivot_table)

from scipy.stats import zscore

df['Amount_zscore'] = zscore(df['Amount'])
outliers = df[df['Amount_zscore'].abs() > 3]
print(f"Outliers detected: {outliers.shape[0]}")

corr_matrix = df[['Amount', 'Product Category_Electronics', 'Product Category_Clothing',
                  'Product Category_Groceries', 'Product Category_Books']].corr()
print(corr_matrix)

category_payment_method_distribution = df.groupby(['Product Category_Electronics', 'Payment Method_Credit Card']).size().unstack()
category_payment_method_distribution.plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Product Category vs Payment Method Distribution')
plt.xlabel('Product Category')
plt.ylabel('Transaction Count')
plt.show()
