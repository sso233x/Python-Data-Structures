def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    
    # Ensure the end index does not exceed the length of the list
    end = min(end, len(nums))
    
    # Calculate the sum from start to end (exclusive)
    return sum(nums[start:end])

nums = [1, 2, 3, 4]
print(sum_range(nums))  
print(sum_range(nums, 1))  
print(sum_range(nums, end=2)) 
print(sum_range(nums, 1, 3))  
print(sum_range(nums, 1, 99))  
