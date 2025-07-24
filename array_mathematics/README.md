# Array Mathematics

## Problem Description
Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.
Task
You are given two integer arrays,  and  of dimensions X. 
Your task is to perform the following operations:
Note 
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
Input Format
The first line contains two space separated integers,  and . 
The next  lines contains  space separated integers of array . 
The following  lines contains  space separated integers of array .
Output Format
Print the result of each operation in the given order under Task.
Sample Input
Sample Output

## Example Input/Output
### Sample Input
```
1 4
1 2 3 4
5 6 7 8
```
### Sample Output
```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
```
