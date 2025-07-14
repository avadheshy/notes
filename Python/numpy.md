# NumPy Essentials for Python Developers

## 1. NumPy Arrays (`ndarray`)

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)         # [1 2 3]
print(type(a))   # <class 'numpy.ndarray'>
```

## 2. Array Creation Functions

```python
np.zeros((2, 3))         # [[0. 0. 0.], [0. 0. 0.]]
np.ones((2, 2))          # [[1. 1.], [1. 1.]]
np.full((2, 2), 7)       # [[7 7], [7 7]]
np.eye(3)                # Identity matrix
np.arange(0, 10, 2)      # [0 2 4 6 8]
np.linspace(0, 1, 5)     # [0.   0.25 0.5  0.75 1. ]
```

## 3. Indexing & Slicing

```python
a = np.array([[10, 20, 30], [40, 50, 60]])
print(a[1, 2])         # 60
print(a[:, 1])         # [20 50]
print(a[0:2, 1:])      # [[20 30], [50 60]]
print(a[a > 25])       # [30 40 50 60]
print(a[[0, 1], [1, 2]])  # [20 60]
```

## 4. Shape and Reshaping

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)          # (2, 3)
b = a.reshape((3, 2))
print(b)
print(b.flatten())      # [1 2 3 4 5 6]

a.shape
(2, 3)

a.ndim
2

```

## 5. Mathematical Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)            # [5 7 9]
print(a * b)            # [ 4 10 18]
print(np.mean(a))       # 2.0
print(np.sum(b))        # 15
```

## 6. Broadcasting

```python
a = np.array([1, 2, 3])
b = 2
print(a + b)            # [3 4 5]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix + a)       # [[2 4 6], [5 7 9]]
```

## 7. Vectorization

```python
a = np.arange(1000000)
b = a * 2               # Vectorized and fast
```

## 8. Random Module

```python
np.random.rand(2, 2)             # Uniform distribution
np.random.randn(2, 2)            # Normal distribution
np.random.randint(0, 10, (2, 3)) # Random integers
```

## 9. Sorting and Searching

```python
a = np.array([3, 1, 2])
print(np.sort(a))             # [1 2 3]
print(np.argsort(a))          # [1 2 0]

a = np.array([10, 20, 30, 40])
print(np.where(a > 25))       # (array([2, 3]),)
```

## 10. Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
print(np.dot(A, B))           # Matrix multiplication
print(np.linalg.inv(A))       # Inverse
print(np.linalg.det(A))       # Determinant

eig_vals, eig_vecs = np.linalg.eig(A)
print(eig_vals)               # Eigenvalues
print(eig_vecs)               # Eigenvectors
```

## 11. Saving and Loading

```python
a = np.array([1, 2, 3])
np.save('my_array.npy', a)
b = np.load('my_array.npy')
print(b)                      # [1 2 3]
```

## 12. NaN and Inf Handling

```python
a = np.array([1, 2, 3, np.nan, np.inf])
print(np.isnan(a))       # [False False False  True False]
print(np.isinf(a))       # [False False False False  True]

# Default nan_to_num behavior:
print(np.nan_to_num(a))
# [1.00000000e+000, 2.00000000e+000, 3.00000000e+000, 0.00000000e+000, 1.79769313e+308]

# Customize replacement values:
print(np.nan_to_num(a, nan=-1, posinf=99999, neginf=-99999))
# [1.0, 2.0, 3.0, -1.0, 99999.0]
```

## 13. Performance Tools

```python
def square(x):
    return x * x

vec_square = np.vectorize(square)
print(vec_square(np.array([1, 2, 3])))  # [1 4 9]

f = lambda i, j: i + j
print(np.fromfunction(f, (3, 3), dtype=int))
# [[0 1 2], [1 2 3], [2 3 4]]
```
