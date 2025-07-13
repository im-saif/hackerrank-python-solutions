# Merge the Tools!

## Problem Description
Consider the following:
We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:
Given  and , print  lines where each line  denotes string .
Example
There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'.  The first substring is all 'A' characters, so .  The second substring has all distinct characters, so .  The third substring has  different characters, so .  Note that a subsequence maintains the original order of characters encountered.  The order of characters in each subsequence shown is important.
Function Description
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
Prints
Print each subsequence on a new line.  There will be  of them.  No return value is expected.
Input Format
The first line contains a single string, . 
The second line contains an integer, , the length of each substring.
Constraints
Sample Input
Sample Output
Explanation
Split  into  equal parts of length . Convert each  to  by removing any subsequent occurrences of non-distinct characters in :
Print each  on a new line.

## Example Input/Output
### Sample Input
```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
```
### Sample Output
```
AB
CA
AD
```
