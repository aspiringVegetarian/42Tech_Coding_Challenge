from HierarchicalSort import hierarchical_sort

print(f"\nHi 42 Technologies, this solution is brought to you by Martynas Vasiliauskas.\n")

demo = input("Whould you like to see a demo using data-big-input.txt sorting on the 'net_sales_units' metric? [y/n]: ")

if demo == "y":
    filename = "./data-big-input.txt"
    metric_to_sort_on = "net_sales_units"
else:
    filename = input("Please provide the full file path of the dataset to be sorted in a hierarchical fashion: ")
    if filename == "":
        filename = "./data-big-input.txt"
    print()
    metric_to_sort_on = input("Please provide the metric you would like to sort on: ")
    if metric_to_sort_on == "":
        metric_to_sort_on = "net_sales_units"
print()

hierarchical_sort(filename, metric_to_sort_on)

print(f"\nHope to hear from you soon!\n")