def BracketMatcher(bracket_expression): 

    # code goes here 
    stack = []
    
    for x in bracket_expression:
        if x == '(':
            stack.append('(')
        elif len(stack) == 0 and x == ')':
            return 0
        elif x == ')':
            stack.pop()
            
    if len(stack) > 0:
        return 0
        
    return 1
    
# keep this function call here  
print BracketMatcher(raw_input())