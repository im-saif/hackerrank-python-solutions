import numpy as np


arr = [int(i) for i in input().split(" ")]
nparr = np.array(arr)
nparr3x3 = np.reshape(nparr, (3,3))
print(nparr3x3)