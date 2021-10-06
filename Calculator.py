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

MISSING_OPERAND: str = "Missing or bad operand"
DIV_BY_ZERO: str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND: str = "Operator not found"
OPERATORS: str = "+-*/^"

class Stack():

<<<<<<< Updated upstream
    def __init__(self):
        self.stack = []

    def top(self):
        if not self.isEmpty():
            return self.stack[0]
        else:
            return -1

    def pop(self):
        self.stack.pop(0)

    def isEmpty(self):
        if len(self.stack) < 1:
            return True
        else:
            return False

    def push(self, ch):
        self.stack.insert(0, ch)

def infix_to_postfix(characters: str):
    s = Stack()
    result = ''

    for ch in characters:
        if isOperand(ch):
            result += ch

        elif ch == ')':
            while not s.isEmpty() and not s.top() == '(':
                result = result + s.top()
                s.pop()
            s.pop()

        elif isOperator(ch):
            while not s.isEmpty() and Higer_precedence(s.top(),ch) and s.top() == '(':
                result = result + str(s.top())
                s.pop()
            s.push(ch)

        elif ch == '(':
            s.push(ch)


    while not s.isEmpty():
        result = result + str(s.top())
        s.pop()

    return result


def Higer_precedence(stack_top, op_2):
    return get_precedence(op_2) > get_precedence(stack_top)


def isOperator(ch):
    if ch == '+' or '-' or '*' or '^' or '/' or ')':
        return True
    else:
        return False

def isOperand(ch):
    isTrue = True
    try:
        int(ch)
    except:
        isTrue = False
    return  isTrue
=======
def infix_to_postfix(tokens):
    return []  # TODO
>>>>>>> Stashed changes


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
<<<<<<< Updated upstream
    #TODO Calculate from RPN
    return 0
=======
    # TODO Calculate from RPN
    operand1: float
    operand2: float
    operator: str

    for i in range(len(postfix_tokens)):
        if postfix_tokens[i] in "+-*/":
            operator = postfix_tokens[i]

            associative = get_associativity(operator)

            if associative == Assoc.LEFT:
                rpn_calculate_left(postfix_tokens, i, operator)

            elif associative == Assoc.RIGHT:
                calc_or_find: bool = find_right_associativity(postfix_tokens, i)
                if calc_or_find:
                    rpn_calculate_right(postfix_tokens, i, operator)
                else:
                    rpn_calculate_left(postfix_tokens, i, operator)

    return postfix_tokens[0]


# Function to calculate from RPN
def remove_used_tokens(postfix_tokens, i):
    postfix_tokens.pop(i)
    postfix_tokens.pop(i - 1)


def rpn_calculate_left(postfix_tokens: list, i: int, operator: str):
    operand1 = postfix_tokens[i - 2]
    operand2 = postfix_tokens[i - 1]
    postfix_tokens[i - 2] = apply_operator(operator, operand1, operand2)

    remove_used_tokens(postfix_tokens, i)


def rpn_calculate_right(postfix_tokens: list, i: int, operator: str):
    operand1 = postfix_tokens[i - 1]
    operand2 = postfix_tokens[i + 1]
    postfix_tokens[i - 1] = apply_operator(operator, operand1, operand2)

    remove_used_tokens(postfix_tokens, i + 2)


# Function to find
def find_right_associativity(postfix_tokens: list, i: int):
    if postfix_tokens[i+2] == "^":
        return True
    else:
        return False
>>>>>>> Stashed changes


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
<<<<<<< Updated upstream
    tokens = expr.split()                                       #Tokens is a list consisting of each char in the original expresion
    #postfix_tokens = infix_to_postfix(tokens)    #Returns the expresion in RTN-format
    #return eval_postfix(postfix_tokens)             #Returns the solution using the interperated RTN-expresion
=======
    tokens = expr.split()
    postfix_tokens = infix_to_postfix(tokens)  # Returns the expresion in RTN-format
    return eval_postfix(postfix_tokens)  # Returns the interperated RTN-expresion
>>>>>>> Stashed changes


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
        "^": 4,
        "(": 5,
        ")": 5
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
    return None  # TODO

# TODO Possibly more methods
