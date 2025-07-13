#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


if __name__ == '__main__':
    s = input()
    d = defaultdict(int)
    for letter in s:
        d[letter] += 1
    sorted_dict = sorted(d.items(), key= lambda x: (-x[1], x[0]))
    for i in range(3):
        print(f"{sorted_dict[i][0]} {sorted_dict[i][1]}")