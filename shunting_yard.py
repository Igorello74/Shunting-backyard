from enum import Enum

class Token:
    NUM = 0
    OPERATOR = 1
    VARIABLE = 2

    def __init__(self, val, token_type):
        self.val = val
        self.token_type = token_type
    
OPERATORS = "^*/+-"

def shunting_yard(inp):
    inp = inp.replace(' ', '')

    tokens = []
    prev = ""
    for i in inp:
        if i.isdigit():
            prev += i

        else:
            if prev:
                tokens.append(Token(prev, Token.NUM))
                prev = ''
                
            if i in OPERATORS:
                tokens.append(Token(i, Token.OPERATOR))
            
            elif i.isalpha():
                tokens.append(Token(i, Token.VARIABLE))
            
    if prev:
        tokens.append(Token(prev, Token.NUM))
    del prev

    output = []
    operators_stack = []

    for i in tokens:
        if i.token_type == Token.NUM:
            output.append(i.val)
        elif i.token_type == Token.OPERATOR:
            op_stack.append
    return tokens


if __name__ == '__main__':
    a = input()
    b = shunting_yard(a)
    for i in b:
        print(f"{i.token_type}:\t{i.val}")
