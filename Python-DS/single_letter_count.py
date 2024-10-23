def single_letter_count(word, letter):
    # Convert both the word and the letter to lowercase for case-insensitive comparison
    word = word.lower()
    letter = letter.lower()
    
    # Count and return the occurrences of the letter in the word
    return word.count(letter)

print(single_letter_count('abracadabra','a'))
print(single_letter_count('succession','s'))