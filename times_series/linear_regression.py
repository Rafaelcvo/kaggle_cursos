"""
link do curso: https://www.kaggle.com/ryanholbrook/linear-regression-with-time-series
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_inline.config import InlineBackend

df = pd.read_csv('datasets/book_sales.csv', index_col='Date', parse_dates=['Date']).drop('Paperback', axis=1)
print(df.head(3))
df['Time'] = np.arange(len(df.index))
print(df.head(2))

