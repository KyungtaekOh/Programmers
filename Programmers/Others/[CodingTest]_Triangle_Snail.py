def solution(n):
    triangle = [[0 for j in range(i,i+i)] for i in range(1,n+1)]
    line, idx, num = -1, 0, 0
    for direc in range(n):
        for step in range(n-direc):
            if direc % 3 == 0:
                line += 1
            elif direc % 3 == 1:
                idx += 1
            elif direc % 3 == 2:
                line -= 1
                idx -= 1
            num += 1
            triangle[line][idx] = num
    answer = sum(triangle, [])
    return answer

"""
Test case
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
"""