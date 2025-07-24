import numpy as np

A = np.array([float(i) for i in input().split(" ")])
x = int(input())

print(np.polyval(A, x))