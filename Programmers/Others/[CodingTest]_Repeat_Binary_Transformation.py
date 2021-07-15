def solution(s):
    answer = [0,0]
    while len(s) != 1:
        cnt = s.count('0')
        s = bin(len(s)-cnt)[2:]
        answer[0] += 1
        answer[1] += cnt
    return answer

"""
s	            result
"110010101001"	[3,8]
"01110"	        [3,3]
"1111111"	    [4,1]
"""