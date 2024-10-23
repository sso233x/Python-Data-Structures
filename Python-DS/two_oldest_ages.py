def two_oldest_ages(ages):
    unique_ages = list(set(ages))
    
    # Sort the unique ages in ascending order
    unique_ages.sort()
    
    # Get the last two ages from the sorted list
    return (unique_ages[-2], unique_ages[-1])


print(two_oldest_ages([1, 2, 10, 8]))  
print(two_oldest_ages([6, 1, 9, 10, 4]))  
print(two_oldest_ages([1, 5, 5, 2]))  
