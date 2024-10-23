def valid_parentheses(parens):
    balance = 0  # Initialize a counter for the balance of parentheses
    
    for char in parens:
        if char == '(':
            balance += 1  
        elif char == ')':
            balance -= 1  
        
        # If balance goes negative, there's a closing parenthesis without a matching opening
        if balance < 0:
            return False
    
    # At the end, balance should be zero for valid parentheses
    return balance == 0

print(valid_parentheses("()")) 
print(valid_parentheses("()()"))  
print(valid_parentheses("(()())"))  
print(valid_parentheses(")()"))  
print(valid_parentheses("())"))  
print(valid_parentheses("((())"))  
print(valid_parentheses(")()("))  
