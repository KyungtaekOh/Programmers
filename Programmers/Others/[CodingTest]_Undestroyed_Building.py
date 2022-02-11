def solution(board, skill):
    answer = 0
    row, col = len(board)+1, len(board[0])+1
    record = [[0 for i in range(col)] for j in range(row)]

    for type, r1, c1, r2, c2, d in skill:
        newd = d if type==2 else -d # degree
        r2, c2 = r2+1, c2+1
        record[r1][c1] += newd      # left, top
        record[r2][c1] += -newd     # right, top
        record[r1][c2] += -newd     # left, bottom
        record[r2][c2] += newd      # right, bottom

    for r in range(1, row):     # row 누적
        for c in range(col):
            record[r][c] += record[r-1][c]

    for r in range(row):        # col 누적
        for c in range(1, col):
            record[r][c] += record[r][c-1]

    for r in range(row-1):      # board에 누적합 적용
        for c in range(col-1):
            board[r][c] += record[r][c]
            answer += 1 if board[r][c]>0 else 0

    return answer

"""
Test case
board	                    skill	                        result
[[5,5,5,5,5],[5,5,5,5,5],   [[1,0,0,3,4,4],[1,2,0,2,3,2],   10
 [5,5,5,5,5],[5,5,5,5,5]]	 [2,1,0,3,1,2],[1,0,1,3,3,1]]	
"""