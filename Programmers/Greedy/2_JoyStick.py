def solution(name):
    count = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer = sum(count)
    idx = 0
    while True:
        count[idx] = 0
        if sum(count) == 0:
            break

        left, right = 1, 1
        while count[idx - left] == 0:
            left += 1
        while count[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer

"""
Test case
name	    return
"JEROEN"	56
"JAN"	    23
"""