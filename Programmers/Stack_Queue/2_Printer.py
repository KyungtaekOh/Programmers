from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        num = queue.popleft()
        if len(queue) == 0:
            answer += 1
            break
        if num < max(queue):
            queue.append(num)
        else:
            answer += 1
            if location == 0:
                break
        location = location-1 if location>0 else len(queue)-1
    return answer

"""
Test case
priorities	        location	return
[2, 1, 3, 2]	    2	        1
[1, 1, 9, 1, 1, 1]	0	        5
"""