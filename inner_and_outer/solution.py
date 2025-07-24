import numpy as np

A = np.array([int(i) for i in input().split(" ")])
B = np.array([int(i) for i in input().split(" ")])

print(np.inner(A, B))
print(np.outer(A, B))