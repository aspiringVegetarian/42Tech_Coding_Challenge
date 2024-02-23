# 42 Technologies Coding Challenge <br> Hierarchical Sorting Solution

## Problem Statement

For this challenge, you must create a sort function that will sort a dataset in a hierarchical manner.
Use your function to sort the `data-big-input.txt` file by `net_sales_units`, from highest to lowest.

## Solution Instructions

The solution is implemented in [hierarchical_sort.py](hierarchical_sort.py).

### Quickstart with main.py

For ease, I have made the [main.py](main.py) file. 

If you clone this repo, you could just simply run main.py, which will ask if you would like to see a demo of the solution by sorting `data-big-input.txt` by `net_sales_units`.

The function will generate the output file `data-big-output.txt` with the sorted data.

If you do not accept the prompt for the demo, it will then prompt you for a filename path and a metric to sort by. 

Similiarly, it will generate an output file with the same name as the filename arguement but "input" will be replaced by "output"

### Function Info

To use the function please import the hierarchical_sort function from [hierarchical_sort.py](hierarchical_sort.py).

The function has the following signature:
```py
def hierarchical_sort(filename: str, metric: str) -> None:
```
The function requires 2 input parameters:
- filename : type string - could be relative or full path
- metric :  type string - must match a metric name in the header of the file 

The function does not return anything, instead it will generate an output file with the same name as the filename arguement but "input" will be replaced by "output".


