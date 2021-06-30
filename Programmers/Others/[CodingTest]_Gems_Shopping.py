def solution(gems):
    gemset = set(gems)
    if len(gemset) == 1: return [1, 1]
    answer, mydict = [0, len(gems)], dict()
    s, e = 0, 0
    while e < len(gems):
        if gems[e] in mydict:
            mydict[gems[e]] += 1
        else:
            mydict[gems[e]] = 1
        if len(mydict) == len(gemset):
            while s <= e:
                if mydict[gems[s]] > 1:
                    mydict[gems[s]] -= 1
                    s += 1
                elif answer[1]-answer[0] > e-s:
                    answer = [s+1, e+1]
                else:
                    break
        e += 1
    return answer

"""
Test case
gems	                                result
["DIA", "RUBY", "RUBY", "DIA",          [3, 7]
 "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
["AA", "AB", "AC", "AA", "AC"]	        [1, 3]
["XYZ", "XYZ", "XYZ"]	                [1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]
"""