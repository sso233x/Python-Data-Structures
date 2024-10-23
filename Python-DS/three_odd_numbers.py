def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        # Calculate the sum of the three sequential numbers
        total = nums[i] + nums[i + 1] + nums[i + 2]
        
        # Check if the sum is odd
        if total % 2 != 0:
            return True  # Return True if an odd sum is found
    
    return False

print(three_odd_numbers([1, 2, 3, 4, 5]))  
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))  
print(three_odd_numbers([5, 2, 1]))  
print(three_odd_numbers([1, 2, 3, 3, 2]))  
