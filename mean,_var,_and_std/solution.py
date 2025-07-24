import numpy as np

n, m = input().split(" ")
n = int(n)
m = int(m)

A = np.array([list(map(int, input().split(" "))) for _ in range(n)])
print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(round(np.std(A), 11))
