def solution(rows, columns, queries):
    answer = []
    coord = [[row*columns+col+1 for col in range(columns)] for row in range(rows)]
    for q in queries:
        x1, y1, x2, y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        min_v = coord[x2][y2]
        rl = coord[x1][y2]

        coord[x1][y1+1:y2+1] = coord[x1][y1:y2]
        min_v = min(min_v, min(coord[x1][y1+1:y2+1]))

        for left in range(x1, x2):
            coord[left][y1] = coord[left + 1][y1]
            min_v = min(min_v, coord[left][y1])

        coord[x2][y1:y2] = coord[x2][y1+1:y2+1]
        min_v = min(min_v, min(coord[x2][y1:y2]))

        for right in range(x2, x1+1, -1):
            coord[right][y2] = coord[right - 1][y2]
            min_v = min(min_v, coord[right][y2])

        coord[x1+1][y2] = rl
        answer.append(min(min_v, rl))
    return answer

"""
Test case
rows    columns queries
6       6       [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
3       3       [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
"""