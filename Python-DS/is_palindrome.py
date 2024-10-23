def is_palindrome(phrase):
    normalized = phrase.replace(" ", "").lower()
    
    # Check if the normalized phrase is equal to its reverse
    return normalized == normalized[::-1]

print(is_palindrome('tacocat'))  
print(is_palindrome('noon'))     
print(is_palindrome('robert'))   
print(is_palindrome('taco cat'))  
print(is_palindrome('Noon'))     

