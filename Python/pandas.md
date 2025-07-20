# Pandas Essentials for Python Developers

## 1. Series and DataFrame

```python
import pandas as pd

s = pd.Series([1, 2, 3])
print(s)
# 0    1
# 1    2
# 2    3

# DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[10, 20])
print(df)
#    A  B
# 0  1  3
# 1  2  4
```

## 2. Reading and Writing Data

```python
# Reading
# CSV file: A,B\n1,3\n2,4

df = pd.read_csv('data.csv')
print(df)
#    A  B
# 0  1  3
# 1  2  4

# Writing
df.to_csv('output.csv', index=False)
```

## 3. Viewing and Exploring Data

```python
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.info()      # Summary of the DataFrame
df.describe()  # Statistics

print(df.shape)     # (2, 2)
print(df.columns)   # Index(['A', 'B'])
print(df.dtypes)    # A: int64, B: int64
print(df.index)     # RangeIndex(start=0, stop=2)
```

## 4. Selecting Data

```python
print(df['A'])     # Column A
print(df.loc[0])   # First row (label)
print(df.iloc[0])  # First row (position)
print(df[df['A'] > 1])
#    A  B
# 1  2  4
df.loc[10]    # works, because 10 is a label
df.iloc[0]    # works, because 0 is a position
df.loc[0]     # ❌ KeyError: 0 is not a label
df.iloc[10]   # ❌ IndexError: only 2 rows, no 10th position

```
- Use loc when you know the index label.

- Use iloc when you want to access by position.
## 5. Filtering & Boolean Indexing

```python
print(df[df['B'] > 3])
#    A  B
# 1  2  4

print(df[(df['A'] > 1) & (df['B'] < 5)])
#    A  B
# 1  2  4
```

## 6. Modifying DataFrames

```python
df['C'] = df['A'] + df['B']
print(df)
#    A  B  C
# 0  1  3  4
# 1  2  4  6

df = df.drop('C', axis=1)
df = df.rename(columns={'A': 'Alpha'})
df = df.replace({0: pd.NA})
print(df)
#    Alpha  B
# 0      1  3
# 1      2  4
```

## 7. Handling Missing Data

```python
df = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
print(df.isnull())
#        A      B
# 0  False  False
# 1   True  False
# 2  False   True

print(df.fillna(0))
#      A    B
# 0  1.0  4.0
# 1  0.0  5.0
# 2  3.0  0.0
```

## 8. Sorting

```python
df = pd.DataFrame({'A': [3, 1, 2], 'B': [9, 8, 7]})
print(df.sort_values(by='A'))
#    A  B
# 1  1  8
# 2  2  7
# 0  3  9
```

## 9. Aggregation and Grouping

```python
df = pd.DataFrame({'A': ['foo', 'bar', 'foo'], 'B': [1, 2, 3]})
print(df.groupby('A').sum())
#       B
# A      
# bar   2
# foo   4
```

## 10. Pivot Tables

```python
df = pd.DataFrame({
    'A': ['foo', 'foo', 'bar'],
    'B': ['one', 'two', 'one'],
    'C': [1, 2, 3]
})
print(df.pivot_table(index='A', columns='B', values='C', aggfunc='sum'))
# B    one  two
# A            
# bar   3  NaN
# foo   1  2.0
```

## 11. Apply and Lambda

```python
df = pd.DataFrame({'A': [1, 2, 3]})
df['double_A'] = df['A'].apply(lambda x: x * 2)
print(df)
#    A  double_A
# 0  1         2
# 1  2         4
# 2  3         6
```

## 12. Merging and Joining

```python
df1 = pd.DataFrame({'id': [1, 2], 'val1': [10, 20]})
df2 = pd.DataFrame({'id': [1, 2], 'val2': [100, 200]})
print(pd.merge(df1, df2, on='id'))
#    id  val1  val2
# 0   1    10   100
# 1   2    20   200
```

## 12.1. Different Ways to Add/Join/Merge Datasets

### Concatenation

```python
# Row-wise concat (stack vertically)
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})
result = pd.concat([df1, df2], ignore_index=True)
print(result)
#    A
# 0  1
# 1  2
# 2  3
# 3  4
```

### Append (deprecated, use concat)

```python
result = df1.append(df2, ignore_index=True)
```

### Join (merge on index)

```python
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'B': [3, 4]}, index=['x', 'y'])
result = df1.join(df2)
print(result)
#    A  B
# x  1  3
# y  2  4
```

### Merge (based on keys)

```python
df1 = pd.DataFrame({'key': ['K0', 'K1'], 'A': ['A0', 'A1']})
df2 = pd.DataFrame({'key': ['K0', 'K1'], 'B': ['B0', 'B1']})
result = pd.merge(df1, df2, on='key')
print(result)
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
```

### Combine First (for filling nulls from another df)

```python
df1 = pd.DataFrame({'A': [None, 2, None]})
df2 = pd.DataFrame({'A': [1, None, 3]})
print(df1.combine_first(df2))
#      A
# 0  1.0
# 1  2.0
# 2  3.0
```

## 13. Datetime Handling

```python
df = pd.DataFrame({'date': ['2023-01-01', '2023-02-15']})
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
print(df)
#         date  month
# 0 2023-01-01      1
# 1 2023-02-15      2
```

## 14. String Operations

```python
df = pd.DataFrame({'email': ['test@gmail.com', 'admin@yahoo.com']})
print(df['email'].str.extract(r'(\w+)@(\w+)'))
#       0      1
# 0  test  gmail
# 1 admin  yahoo
```

## 15. Efficient Iteration (Avoid loops)

```python
df = pd.DataFrame({'A': [1, 2]})
df['A_squared'] = df['A'].apply(lambda x: x**2)
df['category'] = df['A'].map({1: 'Low', 2: 'Medium'})
print(df)
#    A  A_squared category
# 0  1          1      Low
# 1  2          4   Medium
```

## 16. Exporting Cleaned Data

```python
df.to_csv('cleaned_data.csv', index=False)
df.to_json('data.json', orient='records')
```

## Bonus: Advanced Features

```python
# Categorical for memory
cat_col = pd.Categorical(['small', 'medium', 'large'])

# Binning with qcut
pd.qcut([1, 2, 3, 4, 5], q=3)

# Querying
df = pd.DataFrame({'A': [1, 3, 5], 'B': [2, 4, 6]})
print(df.query('A > 2 & B < 6'))
#    A  B
# 1  3  4
```
