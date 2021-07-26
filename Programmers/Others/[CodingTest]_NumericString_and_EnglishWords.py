def solution(s):
    ndict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
             'six':6, 'seven':7, 'eight':8, 'nine':9, '':''}
    for k, v in ndict.items():
        s = s.replace(k, str(v))
    return int(s)

"""
Test case
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
"""