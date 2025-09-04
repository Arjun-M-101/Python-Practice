'''
NUMPY

NumPy for Data Engineering — The Complete Field Manual.  
Think of it as a *cinematic training montage* for your DE toolkit.  

---

# NumPy for Data Engineering — Field Manual

## 📖 Chapter 1 — Why NumPy Matters in DE
- Foundation Layer: Pandas, scikit‑learn, and many ETL/ML tools are built on NumPy arrays.
- Speed Layer: Vectorized operations run in C under the hood — far faster than Python loops.
- Bridge Layer: Lets you translate Data Science prototypes into DE‑ready transformations.
- Scope for DE:  
  - Quick in‑memory transformations before ingestion.  
  - Data validation and QA checks.  
  - Pre/post‑processing for APIs, ML models, or analytics.

---

## 📖 Chapter 2 — Creating Arrays

### From Python Lists'''
import numpy as np

arr = np.array([1, 2, 3])
print(arr, arr.dtype, arr.shape)

### From Ranges
print(np.arange(0, 10, 2))   # [0 2 4 6 8]
print(np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1. ]

### From Zeros/Ones
print(np.zeros((3, 2)))
print(np.ones((2, 4), dtype=int))

#DE Use Case: Initialize placeholder arrays for batch processing or schema‑aligned buffers.

## 📖 Chapter 3 — Shapes & Dimensions
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)   # 2
print(a.shape)  # (2, 3)
print(a.size)   # 6

#DE Tip: Shape awareness prevents mismatches when merging, reshaping, or exporting.

## 📖 Chapter 4 — Indexing & Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])          # Slice
print(arr[-1])           # Last element
print(arr[[0, 2, 4]])    # Fancy indexing

#Boolean Masking
mask = arr > 25
print(arr[mask])         # [30 40 50]

#DE Use Case: Filter in‑memory datasets before writing to disk.


## 📖 Chapter 5 — Vectorized Operations & Broadcasting
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)     # [11 22 33]
print(x * 10)    # [10 20 30]

#Broadcasting Example
mat = np.array([[1], [2], [3]])
vec = np.array([10, 20, 30])
print(mat + vec)

#DE Use Case: Apply transformations to entire datasets without loops.

## 📖 Chapter 6 — Aggregations & Reductions
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data.sum(axis=0))  # Column sums
print(data.mean(axis=1)) # Row means

#DE Use Case: Quick QA checks — e.g., row counts, totals, averages.

## 📖 Chapter 7 — Reshaping & Type Casting
mat = np.arange(6).reshape(2, 3)
print(mat.astype(float))

#DE Use Case: Reshape data for APIs, ML models, or binary formats.

## 📖 Chapter 8 — I/O with NumPy
np.savetxt('output.csv', mat, delimiter=',', fmt='%d')
loaded = np.loadtxt('output.csv', delimiter=',')

#DE Use Case: Lightweight save/load for intermediate pipeline steps.

## 📖 Chapter 9 — Problem‑Solving Drills

#1. Filter & Transform
arr = np.array([5, 10, 15, 20, 25])
result = arr[arr > 12] * 2
print(result)  # [30 40 50]

#2. Reshape for Batch Processing
data = np.arange(1, 13)
batches = data.reshape(3, 4)
print(batches)

#3. Quick Validation
data = np.array([[1, 2], [3, 4]])
assert data.shape == (2, 2), "Shape mismatch!"
'''
## 📖 Chapter 10 — DE‑Focused Patterns
- Pre‑pandas Filtering: Use NumPy masks before DataFrame creation for speed.
- Schema Validation: Check shapes/dtypes before ingestion.
- Vectorized QA: Run column‑wise checks without loops.
- Memory Efficiency: Use dtype to control memory footprint.

---

## 📖 Chapter 11 — What to Skip (for DE)
- Advanced linear algebra (np.linalg) unless ML‑adjacent.
- Fourier transforms, polynomial fitting, random number generation (unless needed).
- Multi‑dimensional broadcasting beyond 2D unless your pipeline demands it.
'''