def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    # If the phrase is shorter than or equal to n, return it as is
    if len(phrase) <= n:
        return phrase
    
    # Otherwise, truncate the phrase and add ellipses
    return phrase[:n-3] + '...'

print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))  
print(truncate("Yo", 100))  
print(truncate('Cool', 1))  
print(truncate("Woah", 4))  
print(truncate("Woah", 3))  
