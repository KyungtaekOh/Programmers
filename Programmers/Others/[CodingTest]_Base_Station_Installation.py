def solution(n, stations, w):
    answer = 0
    area = [0]
    for i in stations:
        area += [i-w, i+w]
    area += [n+1]
    for idx in range(0, len(area)-1, 2):
        scope = area[idx+1]-area[idx]-1
        d, v = divmod(scope, 2*w+1)
        need = d if v==0 else d+1
        answer += need
    return answer

"""
Test case
N	stations	W	answer
11	[4, 11]	    1	3
16	[9]	        2	3
"""