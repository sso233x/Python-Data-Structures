def sum_pairs(nums, goal):
    seen = set()

    for num in nums:
        # Calculate the complement (what number we need to form the sum)
        complement = goal - num
        
        # If the complement is already in the set, return the pair
        if complement in seen:
            return (complement, num)
        
        # Add the current number to the set of seen numbers
        seen.add(num)

    return ()

print(sum_pairs([1, 2, 2, 10], 4)) 
print(sum_pairs([4, 2, 10, 5, 1], 6)) 
print(sum_pairs([5, 1, 4, 8, 3, 2], 7)) 
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))

