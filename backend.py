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
    
class Node:
    """Represent two operands and an operation symbol."""

    def __init__(self, ar1, operator, ar2):
        self.ar1 = ar1
        self.operator = operator
        self.ar2 = ar2
    
    def __str__(self):
        if type(self.ar1) is Node:
            if get_operator_priority(self.ar1.operator) <= get_operator_priority(self.operator):
                ar1_str = f"({str(self.ar1)})"
            else:
                ar1_str = str(self.ar1)
        else:
            ar1_str = str(self.ar1)

        if type(self.ar2) is Node:
            if get_operator_priority(self.ar2.operator) <= get_operator_priority(self.operator):
                ar2_str = f"({str(self.ar2)})"                
            else:
                ar2_str = str(self.ar2)
        else:
            ar2_str = str(self.ar2)

        return ' '.join((ar1_str, self.operator, ar2_str))


def infix2postfix(inp, string_output=False):
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
    
    
    if string_output:
        return ' '.join(output)
    else:
        return output


def postfix2infix(inp):
    """Convert a postfix (RPN) expression to a conventional infix one.

    Arguments:
    inp -- a list or a string of the Reverse Polish Notation members.
           If a string, each member must be separated with a space.
    """
    try:
        inp = inp.split()
    except AttributeError:
        pass
    
    stack = []

    for i in inp:
        if i in OPERATORS_PRIORITY:
            assert len(stack)>=2, "Operators can't go before operands"
            
            node = Node(stack.pop(-2), i, stack.pop())
            stack.append(node)
        
        elif i.isalnum():
            stack.append(i)
        
        else:
            raise ValueError(f"Unknown character '{i}'")
    
    return(str(stack[0]))


def postfix2prefix(inp, string_output=False):
    """Convert a postfix (RPN) expression to a prefix (PN or NPN) one.

    Arguments:
    inp -- a list or a string of the Reverse Polish Notation members.
           If a string, each member must be separated with a space.
    """

    raise SystemError("UNDER DEVELOPMENT")
    try:
        inp = inp.split()
    except AttributeError:
        pass
    
    stack = []
    output=[]
    for i in inp:
        if i in OPERATORS_PRIORITY:
            assert len(stack)>=2, "Operators can't go before operands"
            
            output.extend()
            stack.append(node)
        
        elif i.isalnum():
            stack.append(i)
        
        else:
            raise ValueError(f"Unknown character '{i}'")


if __name__ == '__main__':
    a = input()
    print(infix2postfix(a))
