import operator
from ArrayStack import ArrayStack


def eval_postfix(exp_lst):

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
    }
    digit_stack = ArrayStack()
    for i in range(len(exp_lst)):
        if exp_lst[i].isdigit():
            digit_stack.push(int(exp_lst[i]))
        elif exp_lst[i] in '+-*/':
            val1 = digit_stack.pop()
            val2 = digit_stack.pop()
            res = ops[exp_lst[i]](val2, val1)
            digit_stack.push(res)
        else:   #exp_lst[i] is a variable name
            pass
    return digit_stack.top()


variables = dict()
loopRunning = True
while loopRunning:
    exp_str = input("--> ")
    exp_lst = exp_str.split()

    for i in range(len(exp_lst)):
        if exp_lst[i] in variables:
            exp_lst[i] = variables[exp_lst[i]]

    if exp_lst[0] == 'done()':
        loopRunning = False
        continue

    if len(exp_lst) == 0:
        pass
    elif len(exp_lst) == 1:
        print(exp_lst[0])
    elif exp_lst[1] == '=':
        variables[exp_lst[0]] = str(eval_postfix(exp_lst[2:]))
        print(exp_lst[0])
    else:
        print(eval_postfix(exp_lst))
