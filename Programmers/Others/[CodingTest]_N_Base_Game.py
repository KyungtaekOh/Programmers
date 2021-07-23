def convert(num, base):
    if num==0:
        return '0'
    alpha = ['A','B','C','D','E','F']
    result = ''
    while num>0:
        num, mod = divmod(num, base)
        if mod >= 10:
            mod = alpha[mod%10]
        result += str(mod)
    return result[::-1]

def solution(n, t, m, p):
    answer, total = '', ''
    num = 0
    while len(total) < t*m:
        total += convert(num, n)
        num += 1
    for idx in range(t):
        answer += total[p-1+(idx*m)]
    return answer

"""
Test case
n	t	m	p	result
2	4	2	1	"0111"
16	16	2	1	"02468ACE11111111"
16	16	2	2	"13579BDF01234567"
"""