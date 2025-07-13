# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(n, blocks):
    stack = []
    l, r = 0, n - 1

    while l <= r:
        chosen = max(blocks[l], blocks[r])
        if len(stack) > 0 and chosen > stack[-1]:
            return "No"

        stack.append(chosen)
        if chosen == blocks[l]:
            l += 1
        else:
            r -= 1
    return "Yes"


T = int(input())
for i in range(T):
    n = int(input())
    blocks = input().split(" ")
    blocks = [int(i) for i in blocks]
    print(solve(n, blocks))