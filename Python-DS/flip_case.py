def flip_case(phrase, to_swap):
    result = ''.join(
        char.lower() if char.upper() == to_swap.upper() else char
        for char in phrase
    )
    
    return result  # Return the modified phrase

print(flip_case('AAaaAAbbBBbb','a'))
print(flip_case('aaAAaaBBbbBB','b'))
