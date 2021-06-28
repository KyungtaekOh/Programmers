def solution(s):
    answer, rotate = 0, len(s)
    for d in range(rotate):
        parenthesis, stack, total = s[d:]+s[:d], [], 0
        for i, pt in enumerate(parenthesis):
            if pt in ['[', '{', '(']:
                idx = ['[', '{', '('].index(pt)
                stack.append(idx)
                total += 1
            else:
                idx = [']', '}', ')'].index(pt)
                if not stack or stack.pop() != idx:break
                total -= 1
            if i == rotate-1 and total == 0:
                answer += 1
    return answer

"""
Test case
s	        result
"[](){}"	3
"}]()[{"	2
"[)(]"	    0
"}}}"	    0
"""