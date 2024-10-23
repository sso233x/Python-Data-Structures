def same_frequency(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Create frequency dictionaries for both numbers
    freq1 = {}
    freq2 = {}
    
    for digit in num1_str:
        freq1[digit] = freq1.get(digit, 0) + 1  # Count digits in num1

    for digit in num2_str:
        freq2[digit] = freq2.get(digit, 0) + 1  # Count digits in num2

    # Compare frequency dictionaries
    return freq1 == freq2

print(same_frequency(551122, 221515))  
print(same_frequency(321142, 3212215))  
print(same_frequency(1212, 2211))   
