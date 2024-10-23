def friend_date(a, b):
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])

    # Check if there is any intersection between the two sets of hobbies
    return bool(hobbies_a & hobbies_b)

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])


print(friend_date(elmo, sauron)) 
print(friend_date(sauron, gandalf)) 