def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda k : (k*4)[:4], reverse=True)
    return str(int(''.join(numbers)))

"""
Test case
numbers	            return
[6, 10, 2]	        "6210"
[3, 30, 34, 5, 9]	"9534330"
"""