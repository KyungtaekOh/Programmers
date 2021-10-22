def solution(line):
    inf = float('inf')
    coord = [inf,-inf,inf,-inf] # minx, maxx, miny, maxy
    points, llen = set(), len(line)
    for i in range(llen):           # 첫번쨰 직선
        a, b, e = line[i]
        for j in range(i, llen):    # 두번쨰 직선
            c, d, f = line[j]
            adbc = (a*d-b*c)
            if adbc==0: continue    # 평행 or 일치
            x = (b*f-e*d)/adbc
            y = (e*c-a*f)/adbc
            if x%1==0 and y%1==0:   # 정수 좌표 확인
                x,y= int(x), int(y)
                points.add((x,y))
                coord[0] = min(coord[0],x)
                coord[1] = max(coord[1],x)
                coord[2] = min(coord[2],y)
                coord[3] = max(coord[3],y)
    answer = [['.' for i in range(coord[1]-coord[0]+1)] for j in range(coord[3]-coord[2]+1)]
    for x, y in points:             # 교점좌표를 *으로 변경
        nx, ny = x-coord[0], coord[3]-y
        answer[ny][nx] = "*"
    return ["".join(l) for l in answer]

"""
Test case
line    [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
result  ["....*....", 
         ".........", 
         ".........", 
         "*.......*", 
         ".........", 
         ".........", 
         ".........", 
         ".........", 
         "*.......*"]
"""