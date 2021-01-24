"""
First solve : 2021-01-24
"""
def solution(triangle):
    cum = [triangle[0]]
    for i, v in enumerate(triangle):
        if i == 0: continue
        temp = []
        for j, v2 in enumerate(v):
            if j == 0:
                temp.append(v2 + cum[i - 1][0])
            elif j == len(v)-1:
                temp.append(v2 + cum[i - 1][-1])
            else:
                temp.append(v2 + max(cum[i-1][j-1], cum[i-1][j]))
        cum.append(temp)
    answer = max(cum[-1])

    return answer


if __name__ == '__main__':
    tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    sol = solution(tri)
    print(sol)
