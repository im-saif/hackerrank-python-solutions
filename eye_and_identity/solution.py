import numpy as np
np.set_printoptions(legacy='1.13')

n, m = input().split(" ")
n = int(n)
m = int(m)
print(np.eye(n, m))


