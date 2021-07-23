from itertools import permutations
def solution(n, weak, dist):
    answer = n
    wlen, dlen = len(weak), len(dist)
    weak.extend([ele + n for ele in weak])  # 1차원 배열로 만들기
    cases = list(permutations(dist, dlen))  # permutatoin
    for idx in range(wlen):
        new_range = weak[idx:idx + wlen]    # weak 출발점 변경
        for case in cases:
            num, count = 0, 1
            poss_dist = new_range[0] + case[num]    # 이동가능 거리
            for weakp in new_range:
                if weakp > poss_dist:       # 이동가능 거리를 지날 경우
                    count += 1
                    if count > dlen:        # 모든 dist를 사용했을 때
                        break
                    num += 1
                    poss_dist = weakp + case[num]
            answer = min(answer, count)
    if answer > dlen:
        answer = -1
    return answer

"""
Test case
n	weak	            dist	        result
12	[1, 5, 6, 10]	    [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	    1
"""