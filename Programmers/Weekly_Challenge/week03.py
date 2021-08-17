from collections import defaultdict, deque
def getShape(board, target, row, col):
    visit, blen = set([(row, col)]), len(board)
    queue = deque([(row,col)])
    shape = [(row,col)]
    while queue:                        # BFS 탐색
        y, x = queue.popleft()
        for r, c in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = y+r, x+c
            if 0<=nr<blen and 0<=nc<blen and (nr,nc) not in visit and board[nr][nc] == target:
                queue.append((nr, nc))
                shape.append((nr, nc))
                visit.add((nr,nc))
    return shape, visit

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

    candi = []
    for step in range(4):           # 4번 반복
        temp = [[0]*size for _ in range(size)]
        for r in range(size):       # 회전
            for c in range(size):
                temp[c][size-1-r] = grid_block[r][c]

        for r in range(size):       # 좌표단위로 변환
            flag = 0
            for c in range(size):
                if temp[r][c] == 1:
                    shape, visit = getShape(temp, 1, r, c)
                    flag = 1
                    break
            if flag == 1:
                break
        shape = move_zero(shape)
        candi.append(shape)
        grid_block = temp
    return min(candi)

# def rotate(block):
#     if len(block) == 1: return block
#     candi = []
#     v = list(map(list, zip(*block)))
#     h, w = max(v[0])-min(v[0]), max(v[1])-min(v[1])
#
#     for not_use in range(4):
#         temp = []
#         for pos in block:
#             temp.append((pos[1], pos[0]))
#         temp = [(r, w-c) for r, c in temp]
#         temp = move_zero(temp)
#         shape = temp
#         candi.append(shape)
#         h, w = w, h
#     return min(candi)

def find_location(board, table):
    blen = len(board)
    bdict, bvisit = defaultdict(list), set()
    tdict, tvisit = defaultdict(list), set()
    for row in range(blen):
        for col in range(blen):
            if board[row][col] == 0 and (row,col) not in bvisit:
                bshape, bvst = getShape(board, 0, row, col)
                bshape = move_zero(bshape)
                bshape = rotate(bshape)
                bdict[len(bshape)].append(bshape)
                for v in bvst:
                    bvisit.add(v)
            if table[row][col] == 1 and (row,col) not in tvisit:
                tshape, tvst = getShape(table, 1, row, col)
                tshape = move_zero(tshape)
                tshape = rotate(tshape)
                tdict[len(tshape)].append(tshape)
                for v in tvst:
                    tvisit.add(v)
    return bdict, tdict

def solution(game_board, table):
    answer = 0
    bdict, tdict = find_location(game_board, table)
    for k, value in bdict.items():
        for loca in value:
            if k not in tdict:
                continue
            for tidx, shape in enumerate(tdict[k]):
                if loca == shape:
                    answer += k
                    del tdict[k][tidx]
    return answer


# print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))
# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))

"""
{6: [[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)], [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 2)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 1)], [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 3)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2)], [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0)]]})
{6: [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1)], [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0)], [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 2)], [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1)], [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (3, 0)], [(0, 0), (0, 1), (1, 0), (1, 1), (2, 1), (3, 1)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1)], [(0, 0), (1, 0), (2, 0), (2, 1), (3, 0), (4, 0)]]})
"""