def intersection(l1, l2):
    return list(set(l1) & set(l2))

print(intersection([1,2,3,4,5,6],[2,4,6,8,10]))
print(intersection([1,2,3,4,5,6],[1,3,5,7,9]))
print(intersection([1,2,3,4,5],[6,7,8,9,10]))