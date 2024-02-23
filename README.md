# 42 Technologies Coding Challenge <br> Hierarchical Sorting Solution

## Problem Statement
For this challenge, you must create a sort function that will sort a dataset in a hierarchical manner.
Use your function to sort the `data-big-input.txt` file by `net_sales_units`, from highest to lowest.

## Solution Instructions
The solution is implemented in [hierarchical_sort.py](hierarchical_sort.py).

To use the function please import the hierarchical_sort function from [hierarchical_sort.py](hierarchical_sort.py. 

The function has the following signature:
```py
hierarchical_sort(filename, metric)
```
The function requires 2 input parameters:
- filename : type string - could be relative or full path
- metric :  type string - must match a metric name in the header of the file 

The function does not return anything, instead it will generate an output file with the same name as the filename arguement but "input" is replaced by "output".
