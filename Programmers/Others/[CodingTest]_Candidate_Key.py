from collections import Counter
from itertools import combinations

def solution(relation):
    answer, cases = [], []
    for i in range(1, len(relation[0])+1):
        cases.extend(combinations(range(len(relation[0])), i))
    for case in cases:
        flag, temp = 0, []
        for key in answer:
            if set(key) & set(case) == set(key): flag = 1
        if flag == 0:
            for row in relation:
                word = ''.join([row[col] for col in case])
                temp.append(word)
            count = Counter(temp).most_common(1)
            if count[0][1] == 1:
                answer.append(case)
    return len(answer)

"""
Test Case  
Relation                            Result
[["100","ryan","music","2"],        2
 ["200","apeach","math","2"],
 ["300","tube","computer","3"],
 ["400","con","computer","4"],
 ["500","muzi","music","3"],
 ["600","apeach","music","2"]]
"""
