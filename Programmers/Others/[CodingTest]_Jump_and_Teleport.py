def solution(n):
    answer = 0
    midpoint = [n]
    hn = n
    while hn > 1:
        if hn % 2 == 0:
            midpoint.append(hn // 2)
            hn = hn // 2
        else:
            midpoint.append(hn - 1)
            midpoint.append(hn // 2)
            hn = (hn - 1) // 2

    curr = 0
    for point in midpoint[::-1]:
        if curr * 2 == point:
            curr *= 2
        elif point - curr == 1:
            curr += 1
            answer += 1

    return answer

def solution2(n):
    return bin(n).count('1')
"""
Test case
N	    result
5	    2
6	    2
5000	5
"""