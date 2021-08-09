def solution(scores):
    answer, slen = '', len(scores)
    grade = ['D', 'D', 'C', 'B', 'A']
    n_score = list(map(list, zip(*scores)))
    for idx, score in enumerate(n_score):
        total, num = sum(score), slen
        if score.count(score[idx])==1 and (max(score)==score[idx] or min(score)==score[idx]):
            total -= score[idx]
            num -= 1
        gidx = int((total/num)//10)-5
        print(total, num, gidx)
        if gidx < 0:
            answer += 'F'
        else:
            answer += grade[gidx]
    return answer

"""
Test case
scores	                                                    result
[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],       "FBABD"
 [61,57,100,80,65],[24,90,94,75,65]]
[[50,90],[50,87]]	                                        "DA"
[[70,49,90],[68,50,38],[73,31,100]]	                        "CFD"
"""