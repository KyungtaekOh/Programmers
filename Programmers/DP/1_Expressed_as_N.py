from collections import deque
def dfs(base, target):
    queue = deque([[0, 0]])
    mins = -1
    while queue:
        curr, step = queue.pop()
        if curr == target and (mins > step or mins == -1):
            mins = step
        elif step > 8:
            continue
        else:
            for i in range(1, 9):
                if step+i > 8: break
                temp = int(str(base)*i)     # 연속된 숫자 만들기
                queue.append([curr + temp, step + i])   # +연산
                queue.append([curr - temp, step + i])   # -연산
                queue.append([curr * temp, step + i])   # *연산
                queue.append([int(curr / temp), step + i])  # /연산
    return mins

def solution(N, number):
    return dfs(N, number)

print(solution(5, 31168))
"""
Test case
N   number  return
5   12      4
5   31168   -1
2   11      3
"""