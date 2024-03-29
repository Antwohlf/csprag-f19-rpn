#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 + arg1
            stack.append(result)
        elif token == '-':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 - arg1
            stack.append(result)
        elif token == '*':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 * arg1
            stack.append(result)
        elif token == '/':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 / arg1
            stack.append(result)
        elif token == '^':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2**arg1
            stack.append(result)
        else:
            stack.append(int(token))

    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
