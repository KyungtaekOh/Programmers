from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for num in course:
        combi = []
        for order in orders:
            com = combinations(sorted(order), num)
            combi += com
        count = Counter(combi)
        if max(count.values()) > 1:
            answer += [''.join(crs) for crs in count if max(count.values()) == count[crs] ]
    return sorted(answer)

"""
Test case
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]     [2, 3, 4]       ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]   [2, 3, 5]       ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]                               [2, 3, 4]       ["WX", "XY"]
"""