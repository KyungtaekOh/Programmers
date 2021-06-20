def divisor(p):
    total = 0
    for idx, c in enumerate(p):
        if c == "(":
            total += 1
        elif c == ")":
            total -= 1
        if idx != 0 and total == 0:
            return p[:idx + 1], p[idx + 1:]
        
def solution(p):
    answer = ''
    if len(p) == 0: return ''
    u, v = divisor(p)
    if u[0] == ")":
        answer = "(" + solution(v) + ")" + ''.join([")" if i == "(" else "(" for i in u[1:-1]])
    elif u[0] == "(":
        answer += u + solution(v)
    return answer

"""
Test case
P           result
"(()())()"	"(()())()"
")("	    "()"
"()))((()"	"()(())()"
"""