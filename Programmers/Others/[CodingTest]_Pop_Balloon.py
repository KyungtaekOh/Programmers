def solution(a):
    answer = 0
    alen = len(a)
    left, right = a[0], a[-1]
    minmax = [[0, ele, 0] for ele in a]     # 왼쪽 최소, a원소, 오른쪽 최소
    for l, r in zip(range(alen), range(len(a) - 1, -1, -1)):
        if left > a[l]:
            left = a[l]
        if right > a[r]:
            right = a[r]
        minmax[l][0] = left
        minmax[r][2] = right

    for idx in range(alen):                 # 왼쪽 최소와 오른쪽 최소 중에서
        left, mid, right = minmax[idx]      # a의 원소보다 큰수가 하나이하 일때
        if left < mid and right < mid:
            continue
        answer += 1

    return answer


"""
Test case
a	                                    result
[9,-1,-5]	                            3
[-16,27,65,-2,58,-92,-71,-68,-61,-33]	6
"""