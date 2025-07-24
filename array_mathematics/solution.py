import numpy as np

n, m = input().split(" ")
n = int(n)
m = int(m)

A = np.array([list(map(int, input().split(" "))) for _ in range(n)])
B = np.array([list(map(int, input().split(" "))) for _ in range(n)])

print(A + B)
print(A - B)
print(A * B)
print(np.floor_divide(A, B))
print(A % B)
print(A ** B)

