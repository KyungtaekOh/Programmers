def solution(s):
    length = len(s)
    answer = length
    for l in range(1, length//2+1):
        prev = s[:l]
        string, count = "", 1
        for i in range(l, length+l, l):
            if prev == s[i:i+l]:
                count += 1
            else:
                if count == 1:
                    string += prev
                else:
                    string += str(count) + prev
                prev = s[i:i+l]
                count = 1
        answer = min(answer, len(string))
    return answer

"""
Test case
7   "aabbaccc"
9   "ababcdcdababcdcd"
8   "abcabcdede"
14  "abcabcabcabcdededededede"
17  "xababcdcdababcdcd"
"""