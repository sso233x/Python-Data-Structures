def find_factors(num):
    factors = []
    
    # Loop through all numbers from 1 to the number itself
    for i in range(1, num + 1):
        # If the current number divides num with no remainder, it's a factor
        if num % i == 0:
            factors.append(i)
    
    return factors

print(find_factors(10))  
print(find_factors(11)) 
print(find_factors(111))  
print(find_factors(321421))  
