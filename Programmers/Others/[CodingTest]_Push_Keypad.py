# 2020 KAKAO 인턴십 - 키패드 누르기
def solution(numbers, hand):
    answer = ''
    pad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    left, right = (0, 3), (2, 3)
    for num in numbers:
        if num % 3 == 1:
            answer += 'L'
            left = (0, pad[0].index(num))
        elif num % 3 == 0 and num!=0:
            answer += 'R'
            right = (2, pad[2].index(num))
        else:
            idx = pad[1].index(num)
            ldist = abs(left[0]-1)+abs(left[1]-idx)
            rdist = abs(right[0]-1)+abs(right[1]-idx)
            if ldist > rdist or (ldist==rdist and hand=="right"):
                answer += "R"
                right = (1, idx)
            elif ldist < rdist or (ldist==rdist and hand=="left"):
                answer += "L"
                left = (1, idx)

    return answer

"""
Test case
numbers	                            hand	    result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	    "LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	    "LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	    "LLRLLRLLRL"
"""