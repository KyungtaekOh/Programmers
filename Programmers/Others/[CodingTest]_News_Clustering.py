from collections import Counter
def solution(str1, str2):
    up1, up2 = str1.upper(), str2.upper()
    set1 = Counter([up1[i:i+2] for i in range(len(up1)-1) if up1[i:i+2].isalpha()])
    set2 = Counter([up2[i:i+2] for i in range(len(up2)-1) if up2[i:i+2].isalpha()])
    inter, union = sum((set1 & set2).values()), sum((set1 | set2).values())
    if union == 0:
        return 65536
    return int(inter/union*65536)

"""
Test case
str1	    str2	        answer
FRANCE	    french	        16384
handshake	shake hands	    65536
aa1+aa2	    AAAA12	        43690
E=M*C^2	    e=m*c^2	        65536
"""