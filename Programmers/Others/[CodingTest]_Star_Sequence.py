from collections import Counter
def solution(a):
    if len(a) < 2: return 0
    answer = 0
    newarr, count = [a[0]], 1
    for ele in a[1:]:               # 연속되고 중복되는 숫자들 최대 2개로 줄이기
        if ele == newarr[-1] and count != 2:
            newarr.append(ele)
            count += 1
        elif ele != newarr[-1]:
            newarr.append(ele)
            count = 1

    if newarr[0] == newarr[1]:      # 1번과 2번이 같을 때 1개로 줄임
        newarr = newarr[1:]
    if newarr[-1] == newarr[-2]:    # -1번과 -2번이 같을 때 1개로 줄임
        newarr = newarr[:-1]

    target = Counter(newarr).most_common(1)[0][0]   # 가장 많은 수
    idx, first, second = 0, -1, -1
    while idx < len(newarr) - 1:    # 스타 수열 찾기
        if (newarr[idx] == newarr[idx + 1]) or (newarr[idx] != target and newarr[idx + 1] != target):
            idx += 1                # target이 되는 수가 없으면 continue
            continue
        answer += 1
        idx += 2

    return answer * 2

"""
Test case
a	                    result
[0]	                    0
[5,2,3,3,5,3]	        4
[0,3,3,0,7,2,0,2,2,0]	8
"""