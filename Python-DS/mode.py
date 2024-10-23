def mode(nums):
    count_dict = {}  # Dictionary to count occurrences of each number
    
    # Count occurrences of each number in nums
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1  # Increment count if num is already in the dictionary
        else:
            count_dict[num] = 1  # Initialize count to 1 if num is new
            
    # Find the number with the maximum count
    most_common = max(count_dict, key=count_dict.get)
    
    return most_common  # Return the most common number

print(mode([1, 2, 1, 2, 1]))        
print(mode([2, 2, 3, 3, 2]))   