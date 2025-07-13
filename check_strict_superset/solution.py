# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(A):
    s = set(input().split(" "))
    for num in s:
        if num not in A:
            return False
    return True


def solver():
    A = set(input().split(" "))
    n = int(input())
    for _ in range(n):
        if not solve(A):
            return False
    return True


print(solver())