import pandas as pd
import numpy as np

# Creating sample sales data
data = {
    'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Region': ['North', 'South', 'East', 'West', 'North', 'East', 'West', 'South', 'North', 'East'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Sales': [100, np.nan, 200, 150, 300, 400, 250, np.nan, 350, 500],
    'Quantity': [10, 15, 20, 25, np.nan, 30, 35, 40, 45, 50]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# 1. Handle missing data: Fill missing 'Sales' with the mean of the column
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# 2. Convert 'Quantity' column to a numeric type, handle errors by coercing (turn invalid data into NaN)
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# 3. Calculate total sales (Sales * Quantity) for each row
df['Total_Sales'] = df['Sales'] * df['Quantity']

# 4. Group by Region and Product to calculate the total sales by group
grouped_sales = df.groupby(['Region', 'Product'])['Total_Sales'].sum().reset_index()

# 5. Merge the sales data with another DataFrame containing product details
product_details = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Category': ['Electronics', 'Clothing', 'Furniture'],
    'Price': [50, 30, 200]
})

# Merging the grouped sales data with the product details
merged_data = pd.merge(grouped_sales, product_details, on='Product', how='left')

# 6. Creating a time series analysis (e.g., calculating rolling average sales over a 3-day window)
df['Rolling_Avg_Sales'] = df['Sales'].rolling(window=3).mean()

# 7. Filter rows where the total sales are greater than a threshold (e.g., $500)
high_sales = merged_data[merged_data['Total_Sales'] > 500]

# 8. Summarize the data: Get total sales by category
total_sales_by_category = merged_data.groupby('Category')['Total_Sales'].sum().reset_index()

# Output results
print("Original Data with Total Sales and Rolling Average:")
print(df)

print("\nGrouped Sales by Region and Product:")
print(grouped_sales)

print("\nMerged Data with Product Details:")
print(merged_data)

print("\nHigh Sales (Total Sales > $500):")
print(high_sales)

print("\nTotal Sales by Category:")
print(total_sales_by_category)
