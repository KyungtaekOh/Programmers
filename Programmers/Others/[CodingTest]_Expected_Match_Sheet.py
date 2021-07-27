def solution(n,a,b):
    answer = 0
    minv = a if a<b else b
    maxv = b if a<b else a
    while maxv-minv>0:
        minv = (minv+1)//2 if minv%2==1 else minv//2
        maxv = (maxv+1)//2 if maxv%2==1 else maxv//2
        answer += 1
    return answer

"""
Test case
N	A	B	answer
8	4	7	3
"""