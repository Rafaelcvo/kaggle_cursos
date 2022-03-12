"""
link do curso: https://www.kaggle.com/ryanholbrook/linear-regression-with-time-series
"""
import pandas as pd

df = pd.read_csv('datasets/book_sales.csv', index_col='Date', parse_dates=['Date']).drop('Paperback', axis=1)
print(df.head(3))