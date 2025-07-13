# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(int)
k = int(input())
rooms = input().split(" ")
for r in rooms:
    d[r] += 1

for r in rooms:
    if d[r] != k:
        print(r)
        break
