from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons, len(dungeons)))
    for case in cases:
        fati, count = k, 0
        for need, consume in case:
            if fati >= need:
                fati -= consume
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer

"""
Test case
k	dungeons	                result
80	[[80,20],[50,40],[30,10]]	3
"""