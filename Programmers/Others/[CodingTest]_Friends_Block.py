def solution(m, n, board):
    answer = 0
    bd = list(map(list,zip(*board)))    # board를 회전
    while True:
        coord = set()
        count = 0
        for r in range(n-1):    # 사라질 블록의 좌표 검색
            for c in range(m-1):
                if bd[r][c]==bd[r+1][c]==bd[r][c+1]==bd[r+1][c+1]!='-':
                    tempset = set([(r,c), (r+1,c), (r,c+1), (r+1,c+1)])
                    coord = coord.union(tempset)
                    count += 1
        if count == 0:  # 사라질 블록이 없는 경우
            break
        answer += len(coord)
        for r, c in coord:  # 사라질 블록 표시
            bd[r][c] = '+'
        for row in range(n):    # 새로운 row을 만들어 갱신
            newline = ['-']*bd[row].count('+')
            newline.extend([ele for ele in bd[row] if ele != '+'])
            bd[row] = newline
    return answer

"""
Test case
m	n	board	                                    answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	    14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA",    15
         "TTMMMF", "TMMTTJ"]	
"""