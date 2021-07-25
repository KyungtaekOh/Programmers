def solution(msg):
    answer = []
    mdict = {chr(65+i): i+1 for i in range(26)}
    msg += '-'
    idx, dict_idx = 0, 27
    while idx < len(msg)-1:
        char = msg[idx]
        while char in mdict:
            if msg[idx]=='-':
                break
            char += msg[idx + 1]
            idx += 1
        answer.append(mdict[char[:-1]])
        mdict[char] = dict_idx
        dict_idx += 1
    return answer


"""
Test case
msg	                        answer
KAKAO	                    [11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	        [1, 2, 27, 29, 28, 31, 30]
"""