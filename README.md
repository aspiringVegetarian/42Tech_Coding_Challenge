# 42 Technologies Coding Challenge <br> Hierarchical Sorting Solution

## Problem Statement

For this challenge, you must create a sort function that will sort a dataset in a hierarchical manner.
Use your function to sort the `data-big-input.txt` file by `net_sales_units`, from highest to lowest.

## Solution Instructions

The solution is implemented in [hierarchical_sort.py](hierarchical_sort.py). The code is well commented and includes a bit of commentary on the big O time complexity. 

### Quickstart with main.py

For ease, I have made the [main.py](main.py) file. 

If you clone this repo, you could just simply change directory into the repo and run main.py. There will be a prompty asking if you would like to see a demo of the solution by sorting `data-big-input.txt` by `net_sales_units`.

The function will create a new text file `sorted_output.txt` with the sorted output dataset. 

If you do not accept the prompt for the demo, it will then prompt you for a filename path and a metric to sort by. 

### Function Info

To use the function please import the hierarchical_sort function from [hierarchical_sort.py](hierarchical_sort.py).

The function has the following signature:
```py
def hierarchical_sort(filename: str, metric: str, delimiter: str = "|", output_filename: str = "./sorted_output.txt") -> None:
```
The function has 2 mandatory input parameters:
- filename : type string - defines the filename of the input dataset. Could be relative or full path.
- metric :  type string - defines the metric to do the hierarchical sort on. Must match a metric name in the header of the file

The function has 2 optional input parameters:
- delimiter : type string - defines the delimiter used in the input dataset and therefore the delimiter used in the output data. Defaults to pipe as defined in the challenge
- output_filename :  type string - defines the filename of the sorted output dataset. Defaults to sorted_output.txt, relative to where the script was ran. 

The function does not return anything.


