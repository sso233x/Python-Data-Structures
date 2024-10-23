def frequency(lst, search_term):
    count = 0  # Initialize a counter
    
    # Iterate through each item in the list
    for item in lst:
        if item == search_term:  # Check if the item matches the search term
            count += 1  # Increment the counter if it matches
            
    return count  # Return the total count

print(frequency([1,2,2,2,3,4,5],2))
print(frequency([1,1,1,1,1,1],1))