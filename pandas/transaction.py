import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate a large dataset with 100,000 transactions
np.random.seed(42)

# Generate sample data
n = 100000
user_ids = np.random.randint(1, 10000, size=n)
categories = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Books'], size=n)
amounts = np.random.gamma(2., 50., size=n)  # Gamma distribution for transaction amounts
payment_methods = np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], size=n)
locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], size=n)
dates = pd.date_range('2023-01-01', periods=n, freq='T')  # Simulating minute-by-minute transactions

# Create a DataFrame
df = pd.DataFrame({
    'Transaction Date': dates,
    'User ID': user_ids,
    'Product Category': categories,
    'Amount': amounts,
    'Payment Method': payment_methods,
    'Location': locations
})

# 1. Data Cleaning
# Remove duplicates (if any)
df = df.drop_duplicates()

# Handle missing values (imagine some values are missing in 'Amount' and 'Location')
df['Amount'] = df['Amount'].fillna(df['Amount'].mean())
df['Location'] = df['Location'].fillna('Unknown')

# 2. Convert categorical columns to numeric using One-Hot Encoding
df = pd.get_dummies(df, columns=['Product Category', 'Payment Method', 'Location'], drop_first=True)

# 3. Time-Series Analysis (Transaction Volume and Value Over Time)
# Resample the data to daily frequency and calculate total amount and transaction count
df.set_index('Transaction Date', inplace=True)
daily_transactions = df.resample('D').agg({'Amount': 'sum', 'User ID': 'nunique'})

# Plot the daily transaction volume and value
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

# 4. Multi-level Grouping and Aggregation
# Group by product category and payment method, then calculate total amount and transaction count
grouped_data = df.groupby(['Product Category_Electronics', 'Payment Method_Credit Card']).agg(
    total_amount=('Amount', 'sum'),
    transaction_count=('Amount', 'size'),
    average_amount=('Amount', 'mean')
).reset_index()

# 5. Rolling Window Analysis (30-day moving average of transaction volume)
df['30_day_moving_avg'] = df['Amount'].rolling(window=30).mean()

# Plot the 30-day moving average of total transaction amounts
df['30_day_moving_avg'].plot(figsize=(14, 6), title='30-Day Moving Average of Transaction Amounts', color='g')
plt.xlabel('Date')
plt.ylabel('Amount (USD)')
plt.show()

# 6. Pivot Table for Transaction Summary by Location and Category
pivot_table = pd.pivot_table(df, values='Amount', 
                             index=['Location_Houston', 'Location_Miami'], 
                             columns=['Product Category_Books', 'Product Category_Electronics'],
                             aggfunc=np.sum, 
                             fill_value=0)

# Display the pivot table
print(pivot_table)

# 7. Outlier Detection (Z-score method)
from scipy.stats import zscore

df['Amount_zscore'] = zscore(df['Amount'])
outliers = df[df['Amount_zscore'].abs() > 3]  # Outliers are defined as values > 3 standard deviations
print(f"Outliers detected: {outliers.shape[0]}")

# 8. Correlation Matrix for Numerical Columns
corr_matrix = df[['Amount', 'Product Category_Electronics', 'Product Category_Clothing',
                  'Product Category_Groceries', 'Product Category_Books']].corr()
print(corr_matrix)

# 9. Visualize Category Distribution of Payment Methods
category_payment_method_distribution = df.groupby(['Product Category_Electronics', 'Payment Method_Credit Card']).size().unstack()
category_payment_method_distribution.plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Product Category vs Payment Method Distribution')
plt.xlabel('Product Category')
plt.ylabel('Transaction Count')
plt.show()
