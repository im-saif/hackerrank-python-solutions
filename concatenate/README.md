# Concatenate

## Problem Description
Concatenate
Two or more arrays can be concatenated together using the concatenate function with a
tuple of the arrays to be joined:
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
Task
You are given two integer arrays of size X and X ( &  are rows, and  is the column).  Your task is to concatenate the arrays along axis .
Input Format
The first line contains space separated integers ,  and . 
The next  lines contains the space separated elements of the  columns. 
After that, the next  lines contains the space separated elements of the  columns.
Output Format
Print the concatenated array of size X.
Sample Input
Sample Output

## Example Input/Output
### Sample Input
```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4
```
### Sample Output
```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
```
