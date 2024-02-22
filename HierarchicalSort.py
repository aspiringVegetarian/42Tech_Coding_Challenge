def hierarchical_sort(filename, metric):
    # read data from file and preprocess each pipe delimited line into its own row
    # special processing for the header
    # O(n) where n is the number of lines in the txt file
    rows = []
    header_proccessed = False
    with open(filename) as f:
        for line in f:
            row = line.rstrip().split('|')
            if not header_proccessed:
                header = row
                header_proccessed = True
                continue
            rows.append(row)
    
            
    
    # find the index of the column we are ulitmately going to sort on
    # count number of properties
    # O(m) where m is the number of columns in the txt file
    num_props = 0
    for col_idx, col_name in enumerate(header):
        if col_name == metric:
            col_idx_to_sort_on = col_idx
            continue
        if "property" in col_name:
            num_props += 1
    
    sorted_rows = sorted(rows, key=lambda row : row[col_idx_to_sort_on], reverse=True)

    print("After first sort")
    print(header)
    for row in sorted_rows:
        print(row)

    total_sorted = []
    for i in range(num_props):
        for row in sorted_rows:
            if row[i] == "$total":
                if i == 0:
                    total_sorted.append(row)
                    break
                else:
                    if row[i-1] == "$total":
                        continue
                    else:
                         total_sorted.append(row)
 


    print("After second sort")
    print(header)
    for row in total_sorted:
        print(row)