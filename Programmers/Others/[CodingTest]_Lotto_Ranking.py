def solution(lottos, win_nums):
    answer = [0, 0]
    win_nums = set(win_nums)
    count, zero = 0, 0
    for num in lottos:
        if num in win_nums:
            count += 1
        elif num == 0:
            zero += 1
    answer[0] = 7-(count+zero) if 7-(count+zero) < 6 else 6
    answer[1] = 7-count if 7-count < 6 else 6
    return answer

"""
Test case
lottos	                win_nums	                result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	    [3, 5]
[0, 0, 0, 0, 0, 0]	    [38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	    [1, 1]
"""