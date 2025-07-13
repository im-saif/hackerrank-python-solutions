# Enter your code here. Read input from STDIN. Print output to STDOUT
lowercase = ""
uppercase = ""
odd = ""
even = ""
s = input()
for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i
    else:
        if i == i.upper():
            uppercase += i
        elif i == i.lower():
            lowercase += i
print("".join(sorted(lowercase)), end="")
print("".join(sorted(uppercase)), end="")
print("".join(sorted(odd)), end="")
print("".join(sorted(even)), end="")