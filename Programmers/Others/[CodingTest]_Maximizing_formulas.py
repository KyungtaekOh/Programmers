from itertools import permutations
from copy import deepcopy

def solution(expression):
    answer = eval(expression)
    ele, prev = [], 0
    for idx, i in enumerate(expression):
        if not i.isdigit():
            ele.append(expression[prev:idx])
            ele.append(i)
            prev = idx + 1
    ele.append(str(expression[prev:]))
    opers = list(permutations(['+','-','*']))

    for priority in opers:
        exp = deepcopy(ele)
        for op in priority[:-1]:
            idx = 1
            while idx < len(exp):
                if exp[idx] == op:
                    exp[idx - 1] = str(eval(exp[idx - 1] + exp[idx] + exp[idx + 1]))
                    del exp[idx:idx + 2]
                else:
                    idx += 2
        answer = max(answer, abs(eval(''.join(exp))))
    return answer

"""
Test case
expression                      result
"100-200*300-500+20"            60420
"200-300-500-600*40+500+500"    1248000
"""