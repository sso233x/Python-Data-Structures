def compact(lst):
    return [item for item in lst if item]

print(compact([0,1,2,'',[],False,True,(),None,'All Done']))
print(compact([True,False,True,False]))