print(f"\nHi 42 Technologies, this solution is brought to you by Martynas Vasiliauskas.\n")

from HierarchicalSort import hierarchical_sort

filename = input("Please provide the full file path of the dataset to be sorted in a hierarchical fashion: ")
if filename == "":
    filename = "./data-small-input.txt"

print()

metric_to_sort_on = input("Please provide the metric you would like to sort on: ")
if metric_to_sort_on == "":
    metric_to_sort_on = "net_sales"

print()

hierarchical_sort(filename, metric_to_sort_on)

print(f"\nHope to hear from you soon!\n")