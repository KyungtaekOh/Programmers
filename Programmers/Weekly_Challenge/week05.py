def solution(word):
    adict, nums = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}, []
    answer, prev = 0, 0
    for i in range(5):
        nums.append(prev + 5 ** i)
        prev += 5 ** i

    for idx, ele in enumerate(word):
        answer += adict[ele] * nums[4 - idx] + 1
    return answer

"""
Test case
word	    result
"AAAAE"	    6
"AAAE"	    10
"I"	        1563
"EIO"	    1189
"""