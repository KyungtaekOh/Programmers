from collections import deque
def solution(s):
    answer, idx = 0, 0
    stack = deque(['-'])
    s += '-'		# s의 마지막 인덱스 확인을 위해 추가
    while idx < len(s)-1:
        if stack[-1] == s[idx]:     # stack과 비교하여 같으면 stack pop
            stack.pop()
        elif s[idx] == s[idx+1]:    # 알파벳이 연속된 경우
            idx += 1
        else:
            stack.append(s[idx])
        idx += 1
    if len(stack)==1:   # stack에 0만 있는 경우 정답
        answer = 1
    return answer

"""
Test case
s           result
baabaa      1
cdcd        0
"""