# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    word = input()
    d[word] += 1

print(len(d.items()))
for (key, value) in d.items():
    print(value, end=" ")