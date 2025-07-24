import numpy as np

n, m = input().split(" ")
n = int(n)
m = int(m)

A = np.array([list(map(int, input().split(" "))) for _ in range(n)])
print(np.prod(np.sum(A, axis=0)))