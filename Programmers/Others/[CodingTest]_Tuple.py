def solution(s):
    answer, mydict = [], []
    temp = s[2:-2].split('},{')
    if len(temp) == 1: return [int(temp[0])]
    for i in temp:
        mydict.append(set(i.split(',')))
    mydict = sorted(mydict, key=lambda k : len(k))
    for idx in range(len(mydict)-1, 0, -1):
        ele = mydict[idx] - mydict[idx-1]
        answer.insert(0, int(ele.pop()))
    answer.insert(0, int(mydict[0].pop()))
    return answer

from collections import Counter
def solution_ver2(s):
    answer, mydict = [], []
    temp = s[2:-2].split('},{')
    for i in temp:
        mydict += i.split(',')
    count = Counter(mydict)
    return [int(k) for k, v in count.most_common()]

"""
Test case
s                               result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	            [111, 20]
"{{123}}"	                    [123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
"""