# package calculator

from collections import deque
from math import nan
from enum import Enum

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"


def infix_to_postfix(tokens):
    output_list = []
    op_stack = []
    #TODO THE FIRST OPERATOR WON'T BE ABLE TO APPEND TO THE OP_STACK WITH CURRENT LOGIC, fix
    for token in tokens:

        if isNumber(token):            #If the token is a number add it to the op_list
            output_list.append(token)

        elif isOperator(token):     #Whatch method token_is_operator(), for details
            token_is_operator(token, op_stack, output_list)

        elif token == '(':              #If the token is a '(' add it to the output
            op_stack.append(token)

        elif token == ')':
            if len(op_stack) > 0:     #If there are operators in the operator stack
                while op_stack[-1] != '(': #Aslong as the top object isn't a '('
                        output_list.append(op_stack[-1])    #Add to output
                        op_stack.pop(-1)                                   #Then remove from op_stack

                if op_stack[-1] == '(':     #If the current stack op is a '('
                    op_stack.pop(-1)            #Remove it

            else:                              #If their are no operators we are  missing operators
                print(MISSING_OPERATOR)
                break

    #When we have placed all tokens in either the op_stack or output_list
    #We are to empty the op_stack
    while len(op_stack) > 0:
        if op_stack[-1] != '(':                     #Aslogn as the
            output_list.append(op_stack[-1])    #Add to output
            op_stack.pop(-1)                                #remove from op_stack

        elif op_stack[-1] ==  ')':
            #If we have a ')' at this stage we can be certain we are missing a '('
            print(MISSING_OPERATOR)
            break

    return output_list

#If the token is an operator that is not a parentheses  this will be called upon in
#the infix_to_postfix() method.
def token_is_operator(token, op_stack, output_list):
    if len(op_stack) > 0:   #If the op_stack contains anything

        #While loop is ran when the stack_operator has higher precedence then the incoming
        #operator. IT will also be run if the operators have equal precedence and the incoming
        # operator isn't a '^' (potenser)
        while (op_stack[-1] != '(' and ((get_precedence(op_stack[-1]) > get_precedence(token)) or
               (get_precedence(op_stack[-1]) == get_precedence(token))  and get_associativity(token) == Assoc.LEFT)):

            output_list.append(op_stack[-1]) #Add the stack operator to the output
            op_stack.pop(-1) #Then remove it from the operator-stack



# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    return 0  # TODO


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    tokens = tokenize(expr)
    postfix_tokens = infix_to_postfix(tokens)
    print(postfix_tokens)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str):
    tmp = ""
    result = []
    for i in range(len(expr)):

        if isNumber(expr[i]) or expr[i] == '.':
            tmp += expr[i]

        elif isOperator(expr[i]):
            if not tmp == "":
                result.append(tmp)
            result.append(expr[i])
            tmp = ""

        # For the last index of the list
        if i == len(expr) - 1 and not tmp == "":
            result.append(tmp)
            tmp = ""

    return result


def isOperator(token):
    if token == '+' or '-' or '*' or '^' or '/' or ')' or '(':
        return True
    else:
        return False


def isNumber(token):
    isTrue = True
    try:
        float(token)
    except:
        isTrue = False
    return isTrue


if __name__ == "__main__": #ONLY RUN THIS FOR TESTING
    tokens = tokenize("(3+5)")
    print(tokens)
    result = infix_to_postfix(tokens)
    print(result)