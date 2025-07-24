import numpy as np

n, m = input().split(" ")
n = int(n)
m = int(m)

nparr = np.array([list(map(int, input().split(" "))) for _ in range(n)])
print(np.transpose(nparr))
print(nparr.flatten())
