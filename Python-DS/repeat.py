def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None
    
    # Return the phrase repeated num times
    return phrase * num

print(repeat('*', 3))  
print(repeat('abc', 2))  
print(repeat('abc', 0))  
print(repeat('abc', -1) is None)  
print(repeat('abc', 'nope') is None) 

