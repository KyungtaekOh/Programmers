def solution(arr):
    def find(r1, c1, r2, c2):
        count = 0
        for line in arr[r1:r2]:         # 범위내 모든 값 sum
            count += sum(line[c1:c2])

        if count == 0:                  # 모두 0일 경우
            return [1, 0]
        elif count == (r2-r1) * (r2-r1):  # 모두 1일 경우
            return [0, 1]
        else:                           # 섞여 있을 경우
            result = [0, 0]
            hl = (r2-r1) // 2
            for dx, dy in [(0, 0), (0, hl), (hl, 0), (hl, hl)]:
                nr1, nc1 = r1 + dx, c1 + dy
                nr2, nc2 = (r1 + r2)//2 + dx, (c1 + c2)//2 + dy
                temp = find(nr1, nc1, nr2, nc2)
                for i in range(2):
                    result[i] += temp[i]
            return result
    alen = len(arr)
    return find(0,0,alen,alen)

"""
Test case
arr     [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
result  [4,9]
"""