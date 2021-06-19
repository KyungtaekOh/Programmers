import math
def solution(w,h):
    if w == 1 or h == 1:
        return 0
    gcd = math.gcd(w, h)
    mw, mh = w / gcd, h / gcd # 2, 3
    num_box, prev = 0, 0
    for idx in range(1, int(mw)+1):
        curr = mh / mw * idx
        num_box += math.ceil(curr) - math.floor(prev)
        prev = curr
    no_use = (w // mw) * num_box
    return (w*h)-no_use

"""
Test case
w   h   return
8   12  80
3   3   6
"""