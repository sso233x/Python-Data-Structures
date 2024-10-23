def list_check(lst):
    for item in lst:
        # Check if the type of item is not list
        if type(item) != list:
            return False

    # If no items failed the check, return True
    return True

print(list_check([[1], [2, 3]]))  
print(list_check([[1], "nope"]))  
