# src/rpn.py

def eval_rpn(tokens):
    """
    Evaluate a Reverse Polish Notation (RPN) expression.
    
    Args:
        tokens (List[str]): RPN tokens, e.g. ["2", "1", "+", "3", "*"]
    
    Returns:
        int: The result of the RPN expression
    """
    stack = []
    
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            # If token is a number, push it onto the stack
            stack.append(int(token))
        else:
            # Operator: pop two operands
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Division truncates toward zero
                stack.append(int(a / b))
    
    # The final result is the only item left in the stack
    return stack[0]
