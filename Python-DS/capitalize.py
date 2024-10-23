def capitalize(phrase):
    if not phrase:  # Check if the phrase is empty
        return phrase
    
    # Capitalize the first letter and combine it with the rest of the phrase
    return phrase[0].upper() + phrase[1:]


print(capitalize('python'))
print(capitalize('hello world!'))