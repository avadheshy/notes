# NumPy Essentials for Python Developers

## 1. NumPy Arrays (`ndarray`)

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)         # [1 2 3]
print(type(a))   # <class 'numpy.ndarray'>
print(a.shape)
print(a.size)
print(a.dtype)
```

### 1.1 Create ndarray with dtype
```python
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype=np.int64)
```

## 2. Array Creation Functions

```python
np.zeros((2, 3))          # [[0. 0. 0.], [0. 0. 0.]]
np.ones((2, 2))           # [[1. 1.], [1. 1.]]
np.full((2, 2), 7)        # [[7 7], [7 7]]
np.eye(3)                 # Identity matrix
np.diag([10, 20, 30, 50]) # Diagonal matrix
np.arange(0, 12, 2)       # [0 2 4 6 8 10]
np.linspace(0, 1, 5)      # [0.  0.25 0.5  0.75 1.]
```

## 3. Indexing & Slicing

```python
a = np.array([[10, 20, 30], [40, 50, 60]])
print(a[1, 2])            # 60
print(a[:, 1])            # [20 50]
print(a[0:2, 1:])         # [[20 30], [50 60]]
print(a[a > 25])          # [30 40 50 60]
print(a[[0, 1], [1, 2]])  # [20 60]

X = np.arange(20).reshape(4, 5)

# Select rows 2–4, columns 3–5
Z = X[1:4, 2:5]

# Select all elements in the 3rd row (rank 1)
v = X[2, :]     # [ 10 11 12 13 14]

# Select all elements in the 3rd column (rank 1)
q = X[:, 2]     # [ 2  7 12 17]

# Select all elements in the 3rd column (rank 2)
R = X[:, 2:3]
```

### 3.1 Mutability

```python
x[3] = 20
X[0, 0] = 20
```

### 3.2 Delete

```python
# np.delete(ndarray, elements, axis)
x = np.array([1, 2, 3, 4, 5])

# Delete the first and fifth element
x = np.delete(x, [0, 4])

Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Delete the first row
w = np.delete(Y, 0, axis=0)

# Delete the first and last column
v = np.delete(Y, [0, 2], axis=1)
```

### 3.3 Append

```python
# np.append(ndarray, elements, axis)
x = np.append(x, 6)          # Append 6
x = np.append(x, [7, 8])     # Append 7 and 8

# Append a new row to Y
v = np.append(Y, [[10, 11, 12]], axis=0)

# Append a new column to Y
q = np.append(Y, [[13], [14], [15]], axis=1)
```

### 3.4 Insert

```python
# np.insert(ndarray, index, elements, axis)
x = np.array([1, 2, 5, 6, 7])
Y = np.array([[1, 2, 3], [7, 8, 9]])

# Insert 3 and 4 between 2 and 5
x = np.insert(x, 2, [3, 4])

# Insert a row between the first and last row of Y
w = np.insert(Y, 1, [4, 5, 6], axis=0)

# Insert a column of 5s between the first and second column of Y
v = np.insert(Y, 1, 5, axis=1)
```

### 3.5 Stacking

```python
# vstack: vertical stacking | hstack: horizontal stacking
# Shapes must match

x = np.array([1, 2])
Y = np.array([[3, 4], [5, 6]])

z = np.vstack((x, Y))           # [[1 2], [3 4], [5 6]]
w = np.hstack((Y, x.reshape(2, 1)))  # [[3 4 1], [5 6 2]]
```

### 3.6 Copy

```python
# Slices are views — use np.copy() to avoid modifying the original
Z = np.copy(X[1:4, 2:5])
W = X[1:4, 2:5].copy()
```

### 3.7 Extract Diagonal Elements

```python
d0 = np.diag(X)        # Main diagonal (k=0)
d1 = np.diag(X, k=1)   # One above main diagonal
d2 = np.diag(X, k=-1)  # One below main diagonal
```

### 3.8 Find Unique Elements

```python
u = np.unique(X)
```

### 3.9 Boolean Indexing

```python
X = np.arange(25).reshape(5, 5)

print(X[X > 10])               # Elements greater than 10
print(X[X <= 7])               # Elements less than or equal to 7
print(X[(X > 10) & (X < 17)]) # Elements between 10 and 17

# Assign -1 to elements between 10 and 17
X[(X > 10) & (X < 17)] = -1
```

## 4. Shape and Reshaping

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)    # (2, 3)
print(a.ndim)     # 2

b = a.reshape((3, 2))
print(b.flatten())  # [1 2 3 4 5 6]
```

## 5. Mathematical Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)         # [5 7 9]
print(a * b)         # [ 4 10 18]
print(np.mean(a))    # 2.0
print(np.sum(b))     # 15

x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])

np.add(x, y)
np.subtract(x, y)
np.multiply(x, y)
np.divide(x, y)

# Element-wise math functions
np.exp(x)
np.sqrt(x)
np.power(x, 2)
```

## 6. Broadcasting

```python
a = np.array([1, 2, 3])

print(a + 2)   # [3 4 5]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix + a)  # [[2 4 6], [5 7 9]]

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x = np.array([1, 2, 3])
Z = np.array([1, 2, 3]).reshape(3, 1)

print(x + X)   # Broadcast row across rows
print(Z + X)   # Broadcast column across columns
```

## 7. Sorting and Searching

```python
# As a function — does not modify original
s = np.sort(x)

# As a method — modifies original in place
x.sort()

# Sort unique elements only
s = np.sort(np.unique(x))

# Sort along columns (axis=0) or rows (axis=1)
s = np.sort(X, axis=0)
s = np.sort(X, axis=1)
```

## 8. Statistical Operations

```python
print(X.mean())           # Mean of all elements
print(X.mean(axis=0))     # Mean of each column
print(X.mean(axis=1))     # Mean of each row
print(X.sum())            # Sum of all elements
print(X.std())            # Standard deviation
print(np.median(X))       # Median
print(X.max())            # Maximum value
print(X.min())            # Minimum value
```

## 9. Set Operations

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 2, 8, 4])

print(np.intersect1d(x, y))  # Elements in both x and y
print(np.setdiff1d(x, y))    # Elements in x but not in y
print(np.union1d(x, y))      # All unique elements of x and y
```

## 10. Random Module

```python
np.random.rand(2, 2)              # Uniform distribution [0, 1)
np.random.randn(2, 2)             # Standard normal distribution
np.random.randint(0, 10, (2, 3)) # Random integers
np.random.randint(4, 15, size=(3, 2))
```

## 11. Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print(np.dot(A, B))          # Matrix multiplication
print(np.linalg.inv(A))      # Inverse
print(np.linalg.det(A))      # Determinant

eig_vals, eig_vecs = np.linalg.eig(A)
print(eig_vals)              # Eigenvalues
print(eig_vecs)              # Eigenvectors
```

## 12. NaN and Inf Handling

```python
a = np.array([1, 2, 3, np.nan, np.inf])

print(np.isnan(a))   # [False False False  True False]
print(np.isinf(a))   # [False False False False  True]

# Default replacement
print(np.nan_to_num(a))

# Custom replacement values
print(np.nan_to_num(a, nan=-1, posinf=99999, neginf=-99999))
```

## 13. Save and Load

```python
a = np.array([1, 2, 3])

np.save('my_array', a)
b = np.load('my_array.npy')
print(b)  # [1 2 3]
```

## 14. Performance Tools

```python
def square(x):
    return x * x

vec_square = np.vectorize(square)
print(vec_square(np.array([1, 2, 3])))  # [1 4 9]

f = lambda i, j: i + j
print(np.fromfunction(f, (3, 3), dtype=int))
# [[0 1 2], [1 2 3], [2 3 4]]
```