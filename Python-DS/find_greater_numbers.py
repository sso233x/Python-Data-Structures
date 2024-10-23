def find_greater_numbers(nums):
    count = 0  # Initialize a counter

    # Loop through each number in the list, except for the last one
    for i in range(len(nums) - 1):
        # Check the numbers that come after the current number
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:  # If a greater number is found
                count += 1  # Increment the counter

    return count

print(find_greater_numbers([1,2,3]))
print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([5,4,3,2,1]))