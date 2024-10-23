def extract_full_names(people):
    return [f"{person['first']} {person['last']}" for person in people]


names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'}
]

print(extract_full_names(names))