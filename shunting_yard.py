from enum import Enum

class Token:
    NUM = 0
    OPERATOR = 1
    CONSTANT = 2

    def __init__(self, val, token_type):
        self.val = val
        self.token_type = token_type
    
operators = "+-*/^"

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
                
            if i in operators:
                tokens.append(Token(i, Token.OPERATOR))
            
    if prev:
        tokens.append(Token(prev, Token.NUM))
    del prev

    output = []
    op_stack = []
    for i in tokens:
        if i.token_types == Token.NUM:
            output.append(i.val)
        elif i.token_types == Token.OPERATOR:
            op_stack.append
    return tokens


if __name__ == '__main__':
    a = input()
    print(shunting_yard(a))
