from itertools import permutations
import math
def solution(numbers):
    answer = 0
    candi = set()
    for i in range(1, len(numbers) + 1):
        candi = candi.union(set(int(''.join(ele)) for ele in list(permutations(numbers, i))))
    candi -= {0, 1}

    for num in candi:
        for div in range(2, int(math.sqrt(num)) + 1):
            if num % div == 0:
                break
        else:
            answer += 1
    return answer

"""
Test case
numbers	    return
"17"	    3
"011"	    2
"""