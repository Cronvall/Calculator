# package calculator
import Calculator


#   A command line interface for the Calculator
#   REPL = Read Eval Print Loop
#
#   **** NOTHING TO DO HERE ****
def program():
    preamble()
    repl_loop()
    goodbye()


def repl_loop():
    while True:
        command = get_input()
        if command == "bye":
            break
        evaluate_command(command)


def evaluate_command(command):
    try:
        result = Calculator.eval_expr(command)
        print(result)
    except NotImplemented as ex:
        print(ex)


def get_input():
    command = input("> ")
    return command


def preamble():
    print("Calculator v 1.0. To exit input bye")


def goodbye():
    print("Have a nice day!")


if __name__ == "__main__":
    input = get_input()
    a = Calculator.infix_to_postfix(input)

    print("Postfix:", a)

    result = Calculator.eval_postfix(a)
    print(result)
    #program()
