def sum_floats(nums):
    total = 0.0  
    
    # Iterate through each item in nums
    for num in nums:
        if isinstance(num, float):  # Check if the item is a float
            total += num  # Add the float to total
    
    return total  # Return the sum of floats


print(sum_floats([1.5, 2.4, 'awesome', [], 1])) 
print(sum_floats([1, 2, 3])) 
print(sum_floats([1.5,2.5,3.5]))                     