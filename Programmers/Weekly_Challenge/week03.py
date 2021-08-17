from collections import defaultdict, deque
def getShape(board, target, row, col):
    visit, blen = set([(row, col)]), len(board)
    queue = deque([(row,col)])
    while queue:                        # BFS 탐색
        y, x = queue.popleft()
        for r, c in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = y+r, x+c
            if 0<=nr<blen and 0<=nc<blen and (nr,nc) not in visit and board[nr][nc] == target:
                queue.append((nr, nc))
                visit.add((nr,nc))
    return list(visit)

def move_zero(block):                   # (0, 0)에 가장 가깝게 이동
    values = list(map(list, zip(*block)))
    minr, minc = min(values[0]), min(values[1])
    return sorted([(r-minr, c-minc) for r, c in block])

def rotate(block):                  # 4번 회전시켜서 min값을 반환
    if len(block)==1: return block
    block = move_zero(block)
    values = list(map(list, zip(*block)))
    size = max(max(values[0]), max(values[1])) + 1
    grid_block = [[0]*size for _ in range(size)]
    for row, col in block:          # grid 형태로 변환
        grid_block[row][col] = 1

    candi = [block]
    for step in range(3):           # 4번 반복
        temp = [[0]*size for _ in range(size)]
        for r in range(size):       # 회전
            for c in range(size):
                temp[c][size-1-r] = grid_block[r][c]
        for r in range(size):       # 좌표단위로 변환
            flag = 0
            for c in range(size):
                if temp[r][c] == 1:
                    visit = getShape(temp, 1, r, c)
                    flag = 1
                    break
            if flag == 1:break
        shape = move_zero(visit)
        candi.append(shape)
        grid_block = temp
    return min(candi)

def find_location(board, table):
    blen = len(board)
    location, bvisit = [], set()
    tdict, tvisit = defaultdict(list), set()
    for row in range(blen):
        for col in range(blen):
            if board[row][col] == 0 and (row,col) not in bvisit:
                bshape = getShape(board, 0, row, col)
                for v in bshape:
                    bvisit.add(v)
                bshape = rotate(bshape)
                location.append(bshape)
            if table[row][col] == 1 and (row,col) not in tvisit:
                tshape = getShape(table, 1, row, col)
                for v in tshape:
                    tvisit.add(v)
                tshape = rotate(tshape)
                tdict[len(tshape)].append(tshape)
    return location, tdict

def solution(game_board, table):
    answer = 0
    location, tdict = find_location(game_board, table)
    for loca in location:
        k = len(loca)
        if k not in tdict:continue
        for tidx, shape in enumerate(tdict[k]):
            if loca == shape:
                answer += k
                del tdict[k][tidx]
                break
    return answer

"""
game_board	                                    table	                                        result
[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],     [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],	    14
 [1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	     [0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
[[0,0,0],[1,1,0],[1,1,1]]	                    [[1,1,1],[1,0,0],[0,0,0]]	                    0
"""