def calculate(operation, a, b, make_int=False, message='The result is'):
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None
    }

    # Check if the provided operation is valid
    if operation not in operations or operations[operation] is None:
        return None
    
    # Perform the operation
    result = operations[operation]
    
    # Truncate result if make_int is True
    if make_int:
        result = int(result)

    # Return the result with the message
    return f"{message} {result}"

print(calculate('add', 2.5, 4)) 
print(calculate('subtract', 4, 1.5, make_int=True)) 
print(calculate('multiply', 1.5, 2)) 
print(calculate('divide', 10, 4, message='I got'))
print(calculate('foo', 2, 3)) 

