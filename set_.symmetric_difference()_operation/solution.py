# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_count = int(input())
eng_set = set(input().split(" "))

fre_count = int(input())
fre_set = set(input().split(" "))

print(len(eng_set.symmetric_difference(fre_set)))