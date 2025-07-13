# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
A = set(input().split(" "))
other = int(input())
for i in range(other):
    inp = input()
    op = inp.split(" ")[0]
    newset = set(input().split(" "))
    if op == "intersection_update":
        A.intersection_update(newset)
    elif op == "update":
        A.update(newset)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(newset)
    elif op == "difference_update":
        A.difference_update(newset)
ans = 0
for i in A:
    ans += int(i)
print(ans)