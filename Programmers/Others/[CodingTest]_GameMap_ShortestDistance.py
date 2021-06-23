from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    while True:
        if len(queue) == 0:
            return -1
        curr = queue.popleft()
        if curr[0] == n-1 and curr[1] == m-1:
            return curr[2]
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = curr[0] + x, curr[1] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, curr[2]+1))

"""
Test case
    maps                answer
[[1, 0, 1, 1, 1],       11
 [1, 0, 1, 0, 1], 
 [1, 0, 1, 1, 1], 
 [1, 1, 1, 0, 1], 
 [0, 0, 0, 0, 1]]
"""