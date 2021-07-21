def solution(numbers):
    answer = []
    for num in numbers:
        bnum = bin(num)[2:]
        if bnum.count('0') == 0:        # 모두 1인 경우
            nnum = '0b10' + bnum[1:]
        else:                           # 0이 포함된 경우
            idx = bnum.rfind('0')       # 오른쪽으로 부터 첫번째 0
            if len(bnum[idx+1:]) > 0:   # 0기준 오른쪽 문자열의 길이가 있을 때
                nnum = '0b' + bnum[:idx] + '10' + bnum[idx+2:]
            else:                       # 0기준 오른쪽 문자열의 길이가 없을 때
                nnum = '0b' + bnum[:idx] + '1' + bnum[idx+1:]
        result = int(nnum, 2)
        answer.append(result)
    return answer

"""
numbers	    result
[2,7]	    [3,11]
"""