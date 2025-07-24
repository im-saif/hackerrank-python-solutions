import numpy as np


n = [int(i) for i in input().split(" ")]
print(np.zeros(tuple(n), int))
print(np.ones(tuple(n), int))