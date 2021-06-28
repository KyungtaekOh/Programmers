from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer, cases, infodict = [], [], defaultdict(list)
    for i in range(5):
        cases.extend(combinations(range(4), i))
    for i in info:
        data = i.split(' ')
        for case in cases:
            temp = data.copy()
            for idx in case:
                temp[idx] = '-'
            infodict[''.join([e[0] for e in temp[:4]])].append(int(data[4]))
    for key, values in infodict.items():
        infodict[key] = sorted(values)
    for q in query:
        cond = q.split(' ')
        newq = ''.join([cond[idx][0] for idx in range(0, 7, 2)])
        start, end = 0, len(infodict[newq])
        while start != end and start != len(infodict[newq]):
            mid = (start + end) // 2
            if infodict[newq][mid] >= int(cond[-1]):
                end = mid
            else:
                start = mid + 1
        answer.append(len(infodict[newq]) - start)
    return answer


"""
Test case
info                                    query
["java backend junior pizza 150",       ["java and backend and junior and pizza 100",
 "python frontend senior chicken 210",   "python and frontend and senior and chicken 200",
 "python frontend senior chicken 150",   "cpp and - and senior and pizza 250",
 "cpp backend senior pizza 260",         "- and backend and senior and - 150",
 "java backend junior chicken 80",       "- and - and - and chicken 100",
 "python backend senior chicken 50"]     "- and - and - and - 150"]

result
[1,1,1,1,2,4]
"""