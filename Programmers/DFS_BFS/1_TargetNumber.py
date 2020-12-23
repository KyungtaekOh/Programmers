"""
First solve : 2020-12-21
    - target을 줄이는 방식으로해도 가능할것 같다.
"""

def solution(numbers, target):
    length = len(numbers)
    answer = dfs(numbers, target, 0, 0, length)

    return answer


def dfs(nums, tar, val, cnt, length):
    if (length == cnt):
        if (val == tar):
            return 1
        else:
            return 0

    left = dfs(nums, tar, val + nums[cnt], cnt + 1, length)
    right = dfs(nums, tar, val - nums[cnt], cnt + 1, length)

    return left + right


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = 5

    sol = solution(numbers, target)


