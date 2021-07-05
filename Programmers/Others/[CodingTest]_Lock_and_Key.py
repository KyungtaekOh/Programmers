import numpy as np
def solution(key, lock):
    l, k = len(lock), len(key)
    key, lock = np.array(key), np.pad(np.array(lock), ((k, k), (k, k)))
    for idx in range(4):
        key = np.rot90(key)
        for row in range(0, l+k):
            for col in range(0, l+k):
                lock[row:row+k, col:col+k] += key
                if 2 in lock[k:k+l, k:k+l] or 0 in lock[k:k+l, k:k+l]:
                    lock[row:row+k, col:col+k] -= key
                    continue
                else:
                    return True
    else:
        return False

"""
Test case
key             lock            result
[[0, 0, 0],     [[1, 1, 1],     True
 [1, 0, 0],      [1, 1, 0],
 [0, 1, 1]]	     [1, 0, 1]]
"""