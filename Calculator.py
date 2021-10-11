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

class Stack:

    def __init__(self):
        self.stack = []

    def top(self):
        if not self.is_empty():
            return self.stack[0]
        else:
            return -1

    def pop(self):
        self.stack.pop(0)

    def is_empty(self):
        if len(self.stack) < 1:
            return True
        else:
            return False

    def push(self, ch):
        self.stack.insert(0, ch)

def set_expresion_list(expr):
    tmp = ""
    result = []
    for i in range(len(expr)):
        if isOperand(expr[i]) or expr[i] == '.':
            tmp += expr[i]

        elif isOperator(expr[i]):
            if not tmp == "":
                result.append(tmp)
            result.append(expr[i])
            tmp = ""

        #For the last index of the list
        if i == len(expr) -1 and not tmp == "":
            result.append(tmp)
            tmp = ""

    print("all expresions:",result)
    return result

def infix_to_postfix(characters: list):
    s = Stack()
    result = []

    expressions = set_expresion_list(characters)

    for expr in expressions:
        if isOperand(expr):
            result.append(expr)

        elif expr == ')':
            while not s.is_empty() and not s.top() == '(':
                result.append(s.top())
                s.pop()
            s.pop()

        elif isOperator(expr):
            while not s.is_empty() and s.top() == '(' and higher_precedence(s.top(), expr) :
                result.append(str(s.top()))
                s.pop()
            s.push(expr)

        elif expr == '(':
            s.push(expr)

    while not s.is_empty():
        result.append(str(s.top()))
        s.pop()

    return result


def higher_precedence(stack_top, op_2):
    print("HEJ",stack_top, op_2)
    return get_precedence(op_2) > get_precedence(stack_top)


def isOperator(ch):
    if ch == '+' or '-' or '*' or '^' or '/' or ')' or '(':
        return True
    else:
        return False


def isOperand(ch):
    isTrue = True
    try:
        float(ch)
    except:
        isTrue = False
    return isTrue


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    # TODO Calculate from RPN
    operand1: float
    operand2: float
    operator: str
    i: int = 0

    while i < len(postfix_tokens):

        if len(postfix_tokens) < i:
            i = 0

        if postfix_tokens[i] in "+-*/^":

            operator = str(postfix_tokens[i])

            associative = get_associativity(operator)

            if associative == Assoc.LEFT:
                rpn_calculate(postfix_tokens, i, operator)

            elif associative == Assoc.RIGHT:
                find_more_priorities(postfix_tokens, i, operator)
            i = 0
        else:
            i += 1

    return postfix_tokens[0]


def find_more_priorities(postfix_tokens: list, i: int, operator: str):
    find: bool = find_right_associativity(postfix_tokens, i)
    j: int = i

    while find:
        i += 1
        find = find_right_associativity(postfix_tokens, i)

    rpn_calculate(postfix_tokens, j, operator)


# Function to calculate from RPN
def remove_used_tokens(postfix_tokens, i):
    postfix_tokens.pop(i)
    postfix_tokens.pop(i - 1)


def rpn_calculate(postfix_tokens: list, i: int, operator: str):
    operand1 = float(postfix_tokens[i - 2])
    operand2 = float(postfix_tokens[i - 1])
    postfix_tokens[i - 2] = str(apply_operator(operator, operand1, operand2))

    remove_used_tokens(postfix_tokens, i)


# Function to find
def find_right_associativity(postfix_tokens: list, i: int):
    try:
        if postfix_tokens[i + 1] == "^":
            return True
    except:
        IndexError
    return False


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan

    tokens = expr.split()  # Tokens is a list consisting of each char in the original expresion
    # postfix_tokens = infix_to_postfix(tokens)    #Returns the expresion in RTN-format
    # return eval_postfix(postfix_tokens)             #Returns the solution using the interperated RTN-expresion

    tokens = expr.split()
    postfix_tokens = infix_to_postfix(tokens)  # Returns the expresion in RTN-format
    return eval_postfix(postfix_tokens)  # Returns the interperated RTN-expresion


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d1 - d2,
        "*": d1 * d2,
        "/": nan if d2 == 0 else d1 / d2,
        "^": d1 ** d2
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
