def merge_the_tools(string, k):
    # your code goes here
    curr = ""
    for i in string:
        if len(curr) == k:
            print("".join(set(curr)))
            curr = ""
        curr += i
    print("".join(set(curr)))