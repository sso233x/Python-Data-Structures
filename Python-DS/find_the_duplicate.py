def find_the_duplicate(nums):
    seen = set()  # Create a set to keep track of seen numbers
    
    for num in nums:
        if num in seen:
            return num  # Return the duplicate number
        seen.add(num)  # Add the number to the set if not already seen
    
    return None

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))  
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))  
print(find_the_duplicate([2, 1, 3, 4]) is None)  

