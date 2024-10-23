def number_compare(a, b):
    if a > b:
        return 'a>b'
    if b > a:
        return 'b>a'
    if b == a:
        return 'b==a'

print(number_compare(2,1))
print(number_compare(1,2))
print(number_compare(2,2))