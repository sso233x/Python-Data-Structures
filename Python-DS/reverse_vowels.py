def reverse_vowels(s):
    vowels = "aeiouAEIOU"  # Set of vowels (both lowercase and uppercase)
    s_list = list(s)  # Convert the string to a list for mutability
    i, j = 0, len(s) - 1  # Two pointers, starting from the beginning and end of the string

    while i < j:
        # Move i forward until we find a vowel
        while i < j and s_list[i] not in vowels:
            i += 1
        
        # Move j backward until we find a vowel
        while i < j and s_list[j] not in vowels:
            j -= 1

        # Swap the vowels
        s_list[i], s_list[j] = s_list[j], s_list[i]
        
        # Move pointers inward
        i += 1
        j -= 1

    return ''.join(s_list)  # Convert list back to string

print(reverse_vowels("Hello"))
