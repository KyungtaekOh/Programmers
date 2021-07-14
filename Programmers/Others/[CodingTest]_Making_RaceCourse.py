from collections import deque
def solution(board):
    answer = float('inf')
    blen = len(board)
    queue = deque()
    for start in [(0,0,0,0), (0,0,2,0)]:
        nboard = [[float('inf') for i in range(blen)] for j in range(blen)]
        queue.appendleft(start)
        while queue:
            row, col, prev, cost = queue.popleft()
            for idx, (r, c) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
                nrow, ncol = row + r, col + c
                ncost = cost+600 if idx != prev else cost+100
                if 0<=nrow<blen and 0<=ncol<blen and nboard[nrow][ncol] > ncost and board[nrow][ncol]==0:
                    queue.append([nrow, ncol, idx, ncost])
                    nboard[nrow][ncol] = ncost
        answer = min(answer, nboard[-1][-1])
    return answer

"""
Test case
board	                    result
[[0,0,0],[0,0,0],[0,0,0]]	900
"""