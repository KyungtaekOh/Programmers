def solution(n):
    answer = ''
    nums = ['4','1','2']
    while n > 0:
        answer = nums[n%3] + answer
        n = (n//3)-1 if n%3==0 else n//3
    return answer

"""
Test case
n	result
1	1
2	2
3	4
4	11
"""