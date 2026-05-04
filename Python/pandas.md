# Pandas Essentials for Python Developers

## 1. Series and DataFrame

```python
import pandas as pd

s = pd.Series([1, 2, 3])
print(s)
# 0    1
# 1    2
# 2    3

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[10, 20])
print(df)
#     A  B
# 10  1  3
# 20  2  4
```

## 2. Reading and Writing Data

```python
# CSV
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df.to_excel('output.xlsx', index=False)

# JSON
df = pd.read_json('data.json')
df.to_json('output.json', orient='records')

# SQL / Snowflake
import sqlalchemy
engine = sqlalchemy.create_engine('snowflake://...')
df = pd.read_sql('SELECT * FROM my_table', con=engine)

# Large files — read in chunks to avoid memory issues
chunks = []
for chunk in pd.read_csv('big_file.csv', chunksize=100_000):
    chunks.append(chunk)
df = pd.concat(chunks, ignore_index=True)
```

## 3. Viewing and Exploring Data

```python
df.head()       # First 5 rows
df.tail()       # Last 5 rows
df.info()       # Column types, non-null counts
df.describe()   # Statistics

print(df.shape)    # (rows, cols)
print(df.columns)  # Column names
print(df.dtypes)   # Data types per column
print(df.index)    # Index info
```

## 4. Selecting Data

```python
df['A']           # Single column → Series
df[['A', 'B']]    # Multiple columns → DataFrame

df.loc[10]        # Row by label
df.iloc[0]        # Row by position

df.loc[10, 'A']   # Single value by label
df.iloc[0, 0]     # Single value by position

df.loc[10:20, 'A':'B']   # Slice by label (inclusive)
df.iloc[0:2, 0:2]        # Slice by position (exclusive end)
```

> **Note:** Use `loc` for index labels, `iloc` for integer positions.
> - `df.loc[0]` → ❌ KeyError if `0` is not a label
> - `df.iloc[10]` → ❌ IndexError if fewer than 11 rows

## 5. Filtering & Boolean Indexing

```python
df[df['B'] > 3]

df[(df['A'] > 1) & (df['B'] < 5)]

# isin — filter by list of values
df[df['A'].isin([1, 3])]

# ~ NOT operator
df[~df['A'].isin([1, 3])]

# query — readable alternative
df.query('A > 1 & B < 5')
```

## 6. Modifying DataFrames

```python
# Add column
df['C'] = df['A'] + df['B']

# Drop column
df = df.drop('C', axis=1)

# Rename columns
df = df.rename(columns={'A': 'Alpha'})

# Replace values
df = df.replace({0: pd.NA})

# Reset index
df = df.reset_index(drop=True)

# Set a column as index
df = df.set_index('id')

# Change column data type
df['A'] = df['A'].astype(float)
df['category'] = df['category'].astype('category')  # saves memory

# Reorder columns
df = df[['B', 'A']]
```

## 7. Handling Missing Data

```python
df = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})

# Detect
df.isnull()       # True where NaN
df.notnull()      # True where not NaN
df.isnull().sum() # Count nulls per column

# Drop
df.dropna()                    # Drop rows with any NaN
df.dropna(subset=['A'])        # Drop rows where column A is NaN
df.dropna(how='all')           # Drop rows where ALL values are NaN

# Fill
df.fillna(0)                   # Fill with a constant
df.fillna(method='ffill')      # Forward fill
df.fillna(method='bfill')      # Backward fill
df['A'].fillna(df['A'].mean()) # Fill with column mean
```

## 8. Removing Duplicates

```python
df.duplicated()                       # Boolean mask of duplicate rows
df.drop_duplicates()                  # Remove duplicate rows
df.drop_duplicates(subset=['A'])      # Based on specific column
df.drop_duplicates(keep='last')       # Keep last occurrence
```

## 9. Sorting

```python
df.sort_values(by='A')                        # Ascending
df.sort_values(by='A', ascending=False)       # Descending
df.sort_values(by=['A', 'B'], ascending=[True, False])  # Multi-column sort
df.sort_index()                               # Sort by index
```

## 10. Aggregation and Grouping

```python
df = pd.DataFrame({
    'region': ['East', 'West', 'East', 'West'],
    'sales':  [100, 200, 150, 300],
    'units':  [1, 2, 3, 4]
})

# Basic groupby
df.groupby('region').sum()
df.groupby('region').mean()
df.groupby('region')['sales'].sum()

# Multiple aggregations on multiple columns
df.groupby('region').agg(
    total_sales=('sales', 'sum'),
    avg_units=('units', 'mean'),
    count=('sales', 'count')
)
#         total_sales  avg_units  count
# region
# East            250        2.0      2
# West            500        3.0      2

# Group by multiple columns
df.groupby(['region', 'units']).sum()
```

## 11. Value Counts

```python
df['region'].value_counts()          # Frequency of each value
df['region'].value_counts(normalize=True)  # As proportions
df['region'].nunique()               # Number of unique values
df['region'].unique()                # Array of unique values
```

## 12. Pivot Tables

```python
df = pd.DataFrame({
    'region': ['East', 'East', 'West'],
    'month':  ['Jan', 'Feb', 'Jan'],
    'sales':  [100, 200, 300]
})

df.pivot_table(index='region', columns='month', values='sales', aggfunc='sum')
# month   Feb    Jan
# region
# East   200.0  100.0
# West     NaN  300.0
```

## 13. Apply and Map

```python
df = pd.DataFrame({'A': [1, 2, 3]})

# apply — row or column wise custom function
df['double'] = df['A'].apply(lambda x: x * 2)

# apply on entire DataFrame (axis=1 for row-wise)
df['sum_row'] = df.apply(lambda row: row['A'] + row['double'], axis=1)

# map — element-wise mapping (Series only)
df['label'] = df['A'].map({1: 'Low', 2: 'Medium', 3: 'High'})

# np.where — vectorized if-else (faster than apply)
import numpy as np
df['flag'] = np.where(df['A'] > 2, 'Big', 'Small')
```

> **Tip:** Prefer vectorized operations and `np.where` over `apply` with loops — much faster on large data.

## 14. Merging and Joining

### Merge (key-based)

```python
df1 = pd.DataFrame({'id': [1, 2], 'val1': [10, 20]})
df2 = pd.DataFrame({'id': [1, 2], 'val2': [100, 200]})

pd.merge(df1, df2, on='id')              # Inner join (default)
pd.merge(df1, df2, on='id', how='left')  # Left join
pd.merge(df1, df2, on='id', how='outer') # Full outer join
```

### Concat (stack rows or columns)

```python
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

pd.concat([df1, df2], ignore_index=True)  # Stack vertically
pd.concat([df1, df2], axis=1)             # Stack horizontally
```

### Join (index-based)

```python
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'B': [3, 4]}, index=['x', 'y'])
df1.join(df2)
#    A  B
# x  1  3
# y  2  4
```

### Combine First (fill nulls from another DataFrame)

```python
df1 = pd.DataFrame({'A': [None, 2, None]})
df2 = pd.DataFrame({'A': [1, None, 3]})
df1.combine_first(df2)
#      A
# 0  1.0
# 1  2.0
# 2  3.0
```

## 15. Datetime Handling

```python
df = pd.DataFrame({'date': ['2023-01-01', '2023-06-15']})

df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year']    = df['date'].dt.year
df['month']   = df['date'].dt.month
df['day']     = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()

# Date arithmetic
df['next_month'] = df['date'] + pd.DateOffset(months=1)
df['diff_days']  = (pd.Timestamp('2024-01-01') - df['date']).dt.days

# Filter by date range
df[df['date'] >= '2023-06-01']
```

## 16. String Operations

```python
df = pd.DataFrame({'email': ['test@gmail.com', 'admin@yahoo.com']})

df['email'].str.upper()
df['email'].str.contains('gmail')
df['email'].str.replace('@', '[at]')
df['email'].str.split('@').str[0]     # Get username
df['email'].str.extract(r'(\w+)@(\w+)')
#       0      1
# 0  test  gmail
# 1 admin  yahoo
```

## 17. Efficient Iteration (Avoid Loops)

```python
# ❌ Slow — never use iterrows on large data
for idx, row in df.iterrows():
    df.at[idx, 'new'] = row['A'] * 2

# ✅ Fast — vectorized
df['new'] = df['A'] * 2

# ✅ Fast — apply for custom logic
df['new'] = df['A'].apply(lambda x: x * 2)

# ✅ Fastest — np.where for conditional logic
df['label'] = np.where(df['A'] > 2, 'High', 'Low')
```

## 18. Performance & Memory Optimization

```python
# Check memory usage
df.memory_usage(deep=True)

# Downcast numeric types
df['A'] = pd.to_numeric(df['A'], downcast='integer')

# Use category dtype for low-cardinality string columns
df['region'] = df['region'].astype('category')

# Read only needed columns from CSV
df = pd.read_csv('data.csv', usecols=['A', 'B'])

# Read in chunks for large files
for chunk in pd.read_csv('big_file.csv', chunksize=100_000):
    process(chunk)
```

## 19. Report Generation

```python
import matplotlib.pyplot as plt

# Bar chart from groupby result
summary = df.groupby('region')['sales'].sum()
summary.plot(kind='bar', title='Sales by Region')
plt.tight_layout()
plt.savefig('report.png')

# Styled DataFrame export to Excel
with pd.ExcelWriter('report.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Summary', index=False)

# Export to HTML
df.to_html('report.html', index=False)

# Styled DataFrame in notebook / HTML
styled = df.style \
    .highlight_max(color='lightgreen') \
    .highlight_min(color='salmon') \
    .format({'sales': '${:,.0f}'})
```

## 20. Exporting Cleaned Data

```python
df.to_csv('cleaned_data.csv', index=False)
df.to_json('data.json', orient='records')
df.to_excel('data.xlsx', index=False)
```

## Bonus: Advanced Features

```python
# Binning continuous values
pd.cut(df['A'], bins=3, labels=['Low', 'Mid', 'High'])
pd.qcut(df['A'], q=4)   # Quantile-based bins

# Categorical for memory efficiency
df['size'] = pd.Categorical(['small', 'medium', 'large'], ordered=True)

# Querying (readable filtering)
df.query('A > 2 & B < 6')

# pipe — chain multiple operations cleanly
df.pipe(lambda d: d.dropna()) \
  .pipe(lambda d: d[d['A'] > 0])

# value_counts on multiple columns
df[['region', 'month']].value_counts()
```