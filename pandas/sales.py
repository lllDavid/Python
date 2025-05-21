import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Region': ['North', 'South', 'East', 'West', 'North', 'East', 'West', 'South', 'North', 'East'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Sales': [100, np.nan, 200, 150, 300, 400, 250, np.nan, 350, 500],
    'Quantity': [10, 15, 20, 25, np.nan, 30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

df['Total_Sales'] = df['Sales'] * df['Quantity']

grouped_sales = df.groupby(['Region', 'Product'])['Total_Sales'].sum().reset_index()

product_details = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Category': ['Electronics', 'Clothing', 'Furniture'],
    'Price': [50, 30, 200]
})

merged_data = pd.merge(grouped_sales, product_details, on='Product', how='left')

df['Rolling_Avg_Sales'] = df['Sales'].rolling(window=3).mean()

high_sales = merged_data[merged_data['Total_Sales'] > 500]

total_sales_by_category = merged_data.groupby('Category')['Total_Sales'].sum().reset_index()

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
