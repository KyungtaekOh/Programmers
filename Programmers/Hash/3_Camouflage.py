from collections import defaultdict
def solution(clothes):
    answer = 1
    cdict = defaultdict(int)
    for name, ctype in clothes:
        cdict[ctype] += 1

    for k, v in cdict.items():
        answer *= (v + 1)
    return answer - 1

"""
Test case
clothes	                                                        return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],      5
 ["green_turban", "headgear"]]
[["crowmask", "face"], ["bluesunglasses", "face"],              3
 ["smoky_makeup", "face"]]
"""