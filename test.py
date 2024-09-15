import numpy as np
import scipy as sp
import pandas as pd

print(np.__version__)

arr = np.array([1,2,3,4,5])
print(arr.mean())

a = np.array([[1, 2, 3],
               [4, 5, 6]])
a.shape
a[0] = 10
a
