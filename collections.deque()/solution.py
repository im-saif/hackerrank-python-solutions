# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    inp = input()
    op = inp.split(" ")[0]
    if op == "append":
        d.append(int(inp.split(" ")[1]))
    elif op == "appendleft":
        d.appendleft(int(inp.split(" ")[1]))
    elif op == "pop":
        d.pop()
    elif op == "popleft":
        d.popleft()
for num in d:
    print(num, end=" ")