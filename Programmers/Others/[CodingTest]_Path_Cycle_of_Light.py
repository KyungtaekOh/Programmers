def new_coord(x, y, grid):
    xlen, ylen = len(grid)-1, len(grid[0])-1
    if x < 0:
        x = xlen
    elif x > xlen:
        x = 0
    if y < 0:
        y = ylen
    elif y > ylen:
        y = 0
    return x, y

def solution(grid):
    answer, queue = [], []
    grid_visit = [[[0,0,0,0] for not_use in line] for line in grid] # [상, 하, 좌, 우]
    for i, line in enumerate(grid):
        for j in range(len(line)):
            for step in range(4):
                if grid_visit[i][j][step] == 1:
                    continue
                queue = [(i, j, step, 0)]
                while queue:
                    x, y, d, s = queue.pop()
                    x, y = new_coord(x, y, grid)
                    if grid_visit[x][y][d] == 1:    # visit 확인
                        break
                    else:
                        grid_visit[x][y][d] = 1
                    if (d == 0 and grid[x][y] == "S") or (d == 2 and grid[x][y] == "L") or (d == 3 and grid[x][y] == "R"):
                        queue.append((x - 1, y, 0, s + 1))  # 다음경로 "상"
                    elif (d == 1 and grid[x][y] == "S") or (d == 3 and grid[x][y] == "L") or (d == 2 and grid[x][y] == "R"):
                        queue.append((x + 1, y, 1, s + 1))  # 다음경로 "하"
                    elif (d == 2 and grid[x][y] == "S") or (d == 1 and grid[x][y] == "L") or (d == 0 and grid[x][y] == "R"):
                        queue.append((x, y + 1, 2, s + 1))  # 다음경로 "좌"
                    elif (d == 3 and grid[x][y] == "S") or (d == 0 and grid[x][y] == "L") or (d == 1 and grid[x][y] == "R"):
                        queue.append((x, y - 1, 3, s + 1))  # 다음경로 "우"
                answer.append(s)
    return sorted(answer)

"""
Test case
grid	    result
["SL","LR"]	[16]
["S"]	    [1,1,1,1]
["R","R"]	[4,4]
"""