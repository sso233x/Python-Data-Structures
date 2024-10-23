def is_odd_string(word):
    total = 0  # Initialize the total sum of character positions
    
    for char in word:
        # Calculate position for 'a' (1) to 'z' (26) and 'A' (1) to 'Z' (26)
        position = ord(char.lower()) - ord('a') + 1
        total += position  # Add the position to the total
    
    # Return True if total is odd, otherwise False
    return total % 2 == 1

print(is_odd_string('a'))  
print(is_odd_string('A'))  
print(is_odd_string('aaaa'))  
print(is_odd_string('AAaa'))  
print(is_odd_string('amazing'))  
