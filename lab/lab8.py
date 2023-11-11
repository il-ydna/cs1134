from ArrayStack import *
import operator


def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        result = stack_sum(s)
        s.push(val)
        return val + result


def eval_prefix(exp_str):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
    }
    exp_lst = exp_str.split()
    digit_stack = ArrayStack()
    for i in range(len(exp_lst)-1, -1, -1):
        if exp_lst[i].isdigit():
            digit_stack.push(int(exp_lst[i]))
        else:
            val1 = digit_stack.pop()
            val2 = digit_stack.pop()
            res = ops[exp_lst[i]](val1, val2)
            digit_stack.push(res)
    return digit_stack.top()


def flatten_list(lst):
    s = ArrayStack()
    res_list = []
    for i in range(len(lst)-1, -1, -1):
        s.push(lst[i])
    while len(s) > 0:
        #print(s.top())
        if isinstance(s.top(), int):
            res_list.append(s.pop())
        elif s.top() == []:
            s.pop()
        else:
            temp = s.top()
            s.push(temp[0])
            temp.pop(0)
    return res_list


s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(stack_sum(s))

print(eval_prefix(" - + * 16 5 * 8 4 20"))

lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
print(flatten_list(lst))