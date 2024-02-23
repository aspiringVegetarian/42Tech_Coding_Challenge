def hierarchical_sort(filename: str, metric: str, delimiter: str = "|", output_filename: str = "./sorted_output.txt") -> None:
    # read data from file and preprocess each pipe delimited line into its own row
    # special processing for the header
    # O(n) where n is the number of lines in the txt file
    rows = []
    header_proccessed = False
    with open(filename) as f:
        for line in f:
            row = line.rstrip().split(delimiter)
            if not header_proccessed:
                header = row
                header_proccessed = True
                continue
            rows.append(row)
    
    
    # find the index of the column we are ulitmately going to sort on
    # count number of properties
    # O(m) where m is the number of columns in the txt file
    num_props = 0
    col_idx_to_sort_on = None
    for i, name in enumerate(header):
        if name == metric:
            col_idx_to_sort_on = i
            continue
        if "property" in name:
            num_props += 1
    if not col_idx_to_sort_on:
        raise NameError("The metric you provided does not exist in the header of the input dataset. Please provide a valid metric.") 
    
    # we make a trie to help us do the sorting by grouping
    # the terminator of a path in the trie will be a tuple with the following data:
    # (row index, float value of the desired metric of the row)
    trie = {}
    for i, row in enumerate(rows):
        j = 0
        cur = trie
        while j < num_props-1:
            if row[j] not in cur:
                cur[row[j]] = {}
            cur = cur[row[j]]
            j += 1
        cur[row[j]] = (i, float(row[col_idx_to_sort_on]))
    

    # use our get_top_line helper function to trim the top line total from our trie
    # we store the row index of the top line total in a new list, row_order
    # row_order will store the indicies of the rows in the correct hierarchical sorted order 
    row_order = [get_top_line(trie)[0]]
  
    # call our trie_digger helper function on our trie and pass in the row_order
    # trie digger with recursively sort the sub groups by the metric of choice
    # then appends the row indicies in the correct hierarchical sorted order 
    trie_digger(trie, row_order)


    # call our recombine_data helper function to recombine the rows (pipe delimited) and the header
    ordered_rows = recombine_data(header, rows, row_order, delimiter)

    # create a new txt file as specified in the function arguement
    # write the lines in the correct hierarchical sorted order 
    with open(output_filename, "w") as f:
        for i in range(len(ordered_rows)):
            f.write(ordered_rows[i])
            # ensure we dont have a new line at the bottom of the txt file
            if i < len(ordered_rows)-1:
                f.write("\n")
    
    print(f"You will find your hierarchically sorted data at the following location : {output_filename}")


# O(p) where p is the number of properties
def get_top_line(trie):
    # we hit our trie path terminator, so return the tuple
    if type(trie) is tuple:
        return trie
    else:
        # recursive down until we hit our terminator
        val = get_top_line(trie['$total'])
    # trim the total path from our trie
    del trie['$total']
    return val

# O(n*p*log(n*p)) where n is the number of rows and p is the number of properties and every entry is unique
# in reality, the built-in sort (timsort, O(nlog(n))) is only going to run on a list of the unqiue keys at each level
# the space/stack that the recursion might take up (if there is a very large data set with many unique entries) is more worrisome than the time complextity
def trie_digger(trie, row_order):
    
    # level by level, we will find the top line totals and sort them based on the metric of choice
    sublist = []
    for key in trie:
        # sublist will have tuple with the following information:
        # (key, row index, float value of the desired metric of the row)
        sublist.append((key, *get_top_line(trie[key])))

    # sort on the float value of the desired metric in Descending order
    sublist.sort(key=lambda tuple : tuple[2], reverse=True)
    
    # our sorted sublist allows us to recurse lower in the correct order
    for item in sublist:
        row_idx = item[1]
        next_key = item[0]
        # append the next row index to the row_order list before we recurse further 
        row_order.append(row_idx)
        # we do not recurse further when the next value is a tuple 
        if type(trie[next_key]) is not tuple:
            trie_digger(trie[next_key], row_order)
        

def recombine_data(header, rows, row_order, delimiter):
    ordered_rows = ["|".join(header)]
    for i in row_order:
        # pipe delimited like the input
        ordered_rows.append(delimiter.join(rows[i]))
    return ordered_rows