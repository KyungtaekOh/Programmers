def solution(A, B):
    A, B = sorted(A), sorted(B)
    answer = 0
    a, b = 0, 0
    while a<len(A) and b<len(B):
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    return answer

"""
Test case
A	        B	        result
[5,1,3,7]	[2,2,6,8]	3
[2,2,2,2]	[1,1,1,1]	0
"""