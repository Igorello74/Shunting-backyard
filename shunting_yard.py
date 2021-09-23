from enum import Enum

OPERATORS_PRIORITY = {
    '+': 0, '-': 0, '/': 1, '*': 1, '^': 2
}

def get_operator_priority(op):
    return OPERATORS_PRIORITY.get(op, -1)


class Token:
    NUM = 0
    OPERATOR = 1
    VARIABLE = 2
    BRACKET = 3

    def __init__(self, val, token_type):
        self.val = val
        self.token_type = token_type
    

def shunting_yard(inp):
    inp = inp.replace(' ', '') # delete any spaces

    tokens = []
    prev = ""
    for i in inp:
        if i.isdigit():
            prev += i

        else:
            if prev:
                tokens.append(Token(prev, Token.NUM))
                prev = ''
                
            if i in OPERATORS_PRIORITY:
                tokens.append(Token(i, Token.OPERATOR))
            
            elif i.isalpha():
                tokens.append(Token(i, Token.VARIABLE))
            
            elif i in '()':
                tokens.append(Token(i, Token.BRACKET))
            
            else:
                raise ValueError(f"Unknown character '{i}'")
            
    if prev:
        tokens.append(Token(prev, Token.NUM))
    del prev

    output = []
    operators_stack = []

    for i in tokens:
        if i.token_type in (Token.NUM, Token.VARIABLE):
            output.append(i.val)
        
        elif i.token_type == Token.OPERATOR:
            i_priority = get_operator_priority(i.val)
            while operators_stack and \
              get_operator_priority(operators_stack[-1]) >= i_priority:
                output.append(operators_stack.pop())
            operators_stack.append(i.val)
            
        elif i.val == '(':
            operators_stack.append(i.val)
        elif i.val == ')':
            while operators_stack and operators_stack[-1] != '(':
                output.append(operators_stack.pop())
            operators_stack.pop()
    
    while operators_stack:
        output.append(operators_stack.pop())
    return ' '.join(output)


if __name__ == '__main__':
    a = input()
    print(shunting_yard(a))