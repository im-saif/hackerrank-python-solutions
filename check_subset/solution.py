# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(A, B):
    for num in A:
        if num not in B:
            return False
    return True


T = int(input())
for i in range(T):
    input()
    A = set(input().split(" "))
    input()
    B = set(input().split(" "))
    print(solve(A, B))