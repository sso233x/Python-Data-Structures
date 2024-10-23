def vowel_count(phrase):
    vowels = set('aeiou')
    
    # Initialize an empty dictionary to store the vowel counts
    count = {}
    
    # Iterate through each character in the phrase, converting to lowercase
    for char in phrase.lower():
        # Check if the character is a vowel
        if char in vowels:
            # If it's already in the dictionary, increment the count
            count[char] = count.get(char, 0) + 1
    
    return count

print(vowel_count('rithm school'))  
print(vowel_count('HOW ARE YOU? i am great!'))  
