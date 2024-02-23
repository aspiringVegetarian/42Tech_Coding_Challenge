from hierarchical_sort import hierarchical_sort

def main():
    print(f"\nHi 42 Technologies, this solution is brought to you by Martynas Vasiliauskas.\n")

    demo = input("Whould you like to see a demo using data-big-input.txt sorting on the 'net_sales_units' metric? [y/n]: ")

    filename = "./data-big-input.txt"
    metric_to_sort_on = "net_sales_units"
    
    if demo == "n":
        inputFile = input("Please provide the full file path of the dataset to be sorted in a hierarchical fashion: ")
        if inputFile == "":
            print(f"You did not enter anything, so we will use {filename}")
        else:
            filename = inputFile

        inputMetric = input("Please provide the metric you would like to sort on: ")
        if inputMetric == "":
            print(f"You did not enter anything, so we will use {metric_to_sort_on}")
        else:
            metric_to_sort_on = inputMetric
    
    # just for formatting in the terminal  
    print()

    # call the function that implements the solution
    hierarchical_sort(filename, metric_to_sort_on)

    print(f"\nHope to hear from you soon!\n")

main()