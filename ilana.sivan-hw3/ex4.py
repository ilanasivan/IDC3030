#Write a function which receives as an input argument a string which represents a mathematical formula and evaluates its value. The program will output the result of the evaluation.

#Function signature should be: evaluate_formula(formula).

#The formula is given in prefix notation: https://en.wikipedia.org/wiki/Polish_notation

#Notes:

#The formula will only include numbers and the 4 basic arithmetic operations +, -, *, /. Note that parentheses are not needed when using prefix notation.
#Input numbers can be integers or floats, and may be negative.
#Your result should be accurate for up to (at least) 2 places past the decimal point.
#Every token in the string will be separated from the next token by whitespace(s).

#Hint: Recursion is your best friend here. (Although other methods can work too.)

#Example:
#Given formula = ' + * 5 - 9 3 + 5 / 10 2 ', the equivalent expression using infix notation is (5 * (9 - 3)) + (5 + (10 / 2)) and the code should print 40.

import operator

def evaluate_formula(formula):
    operators = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul, '%': operator.mod}
    stack = []
    for i in reversed(formula.split()):
        if i in operators:
            stack[-2] = operators[i](float(stack[-1]), float(stack[-2]))
            del stack[-1]
        else:
            stack.append(i)
    print(float(stack[0]))
