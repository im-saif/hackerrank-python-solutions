import numpy as np

n, m, p = input().split(" ")
n = int(n)
m = int(m)
p = int(p)

arr1 = np.array([list(map(int, input().split(" "))) for _ in range(n)])
arr2 = np.array([list(map(int, input().split(" "))) for _ in range(m)])

print(np.concatenate((arr1, arr2)))

