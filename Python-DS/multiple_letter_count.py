def multiple_letter_count(phrase):
    frequency = {}  # Initialize an empty dictionary to store letter frequencies

    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the character is a letter (A-Z or a-z)
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            # Increment the count of the letter in the dictionary
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    return frequency

print(multiple_letter_count('abracadabra'))
print(multiple_letter_count('HELLO'))