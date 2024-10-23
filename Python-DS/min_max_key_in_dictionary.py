def min_max_keys(d):
    if not d:  # Check if the dictionary is empty
        return None, None  # Return None for both if empty
    
    min_key = min(d.keys())  # Find the minimum key
    max_key = max(d.keys())  # Find the maximum key
    
    return min_key, max_key  

print(min_max_keys({2:'a',7:'b',1:'c',10:'d',4:'e'}))
print(min_max_keys({'apple':'red','cherry':'red','berry':'blue'}))
print(min_max_keys({}))