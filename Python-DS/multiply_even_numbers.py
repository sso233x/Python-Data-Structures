def multiply_even_numbers(nums):
    product = 1  # Initialize the product to 1
    has_even = False  # Flag to check if there's at least one even number

    # Iterate through each number in the list
    for num in nums:
        if num % 2 == 0:  # Check if the number is even
            product *= num  # Multiply the even number to the product
            has_even = True  # Set the flag to True since we found an even number

    return product if has_even else 1  # Return the product if there are even numbers, else return 1


print(multiply_even_numbers([1,2,3,4,5]))
print(multiply_even_numbers([6,7,8,9,10]))