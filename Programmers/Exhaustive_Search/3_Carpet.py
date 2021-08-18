import math
def solution(brown, yellow):
    brown = (brown+4)/4
    w, h = math.ceil(brown), math.floor(brown)
    while h>2:
        inside = (w-2)*(h-2)
        if inside == yellow:
            return [w, h]
        w += 1
        h -= 1

"""
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]
"""