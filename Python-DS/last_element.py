def last_element(lst):
    if not lst:
        return None  # Return None for an empty list
    return lst[-1]

print(last_element([1, 2, 3])) 
print(last_element([]) is None)  
