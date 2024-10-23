def partition(lst, fn):
    passed = []  # Items that passed the predicate test
    failed = []  # Items that failed the predicate test
    
    # Iterate through each item in the list
    for item in lst:
        if fn(item):  # If the item passes the test
            passed.append(item)  # Add to passed list
        else:
            failed.append(item)  # Add to failed list
            
    return [passed, failed]  # Return the two lists

def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

print(partition([1,2,3,4,5,6,7,8], is_even))
print(partition(['hi', None, 6, 'bye'], is_string))
