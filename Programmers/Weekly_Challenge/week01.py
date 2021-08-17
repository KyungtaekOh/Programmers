def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price*(i+1)
    return total-money if total > money else 0

"""
Test case
price	money	count	result
3	    20	    4	    10
"""