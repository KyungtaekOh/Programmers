def solution(stones, k):
    minp, maxp = 0, 200000000
    while minp <= maxp:
        midp = (maxp + minp) // 2
        count = 0
        for stone in stones:
            if stone <= midp:
                count += 1
            else:
                count = 0
            if count == k:
                answer = midp
                maxp = midp-1
                break
        else:
            minp = midp+1
    return answer

"""
Test case
stones      [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k           3
result      3
"""