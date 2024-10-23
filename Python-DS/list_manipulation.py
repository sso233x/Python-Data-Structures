def list_manipulation(lst, command, location, value=None):
    if command == 'remove':
        if location == 'beginning':
            return lst.pop(0) if lst else None  # Remove and return first item
        elif location == 'end':
            return lst.pop() if lst else None  # Remove and return last item
    elif command == 'add':
        if location == 'beginning':
            lst.insert(0, value)  # Add value to the beginning
            return lst
        elif location == 'end':
            lst.append(value)  # Add value to the end
            return lst
    
    return None  # Return None for invalid commands or locations

print(list_manipulation([1,2,3,4,5],'remove','end'))
print(list_manipulation([1,2,3,4,5],'add','end', 6))
print(list_manipulation([1,2,3,4,5],'add','end'))
