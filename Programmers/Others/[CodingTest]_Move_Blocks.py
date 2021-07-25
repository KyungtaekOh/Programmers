from collections import deque
def coord_check(coord, board):
    blen = len(board) - 1
    if 0 <= coord[0] <= blen and 0 <= coord[1] <= blen and board[coord[0]][coord[1]] == 0:
        return True
    return False

def solution(board):
    answer = 0
    blen = len(board) - 1
    queue = deque([((0, 0), (0, 1), 0)])
    visit = set()
    while queue:
        wing1, wing2, count = queue.popleft()
        if wing1 == (blen, blen) or wing2 == (blen, blen):  # 종료 조건
            answer = count
            break
        if (wing1, wing2) in visit:     # 방문했었다면 continue
            continue
        visit.add((wing1, wing2))

        for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:     # 평행이동
            coord1 = (wing1[0] + x, wing1[1] + y)
            coord2 = (wing2[0] + x, wing2[1] + y)
            if coord_check(coord1, board) and coord_check(coord2, board):
                queue.append((coord1, coord2, count+1))

        for d in [-1, 1]:                                   # 회전
            if wing1[0]==wing2[0]:      # 가로에서 회전
                if coord_check((wing1[0]+d, wing1[1]), board) and coord_check((wing2[0]+d, wing2[1]), board):
                    queue.append((wing1, (wing1[0]+d, wing1[1]), count+1))
                    queue.append((wing2, (wing2[0]+d, wing2[1]), count+1))
            else:                       # 세로에서 회전
                if coord_check((wing1[0], wing1[1]+d), board) and coord_check((wing2[0], wing2[1]+d), board):
                    queue.append((wing1, (wing1[0], wing1[1]+d), count+1))
                    queue.append((wing2, (wing2[0], wing2[1]+d), count+1))

    return answer

"""
Test case
board       [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
result      7
"""