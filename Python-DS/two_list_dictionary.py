def two_list_dictionary(keys, values):
    result = {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}
    
    return result

    
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))  
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))  
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))  
