# Eye and Identity

## Problem Description
identity
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.
eye
The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
Task
Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.
Note
In order to get alignment correct, please insert the line  below the numpy import.
Input Format
A single line containing the space separated values of  and . 
 denotes the rows. 
 denotes the columns.
Output Format
Print the desired X array.
Sample Input
Sample Output

## Example Input/Output
### Sample Input
```
3 3
```
### Sample Output
```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
