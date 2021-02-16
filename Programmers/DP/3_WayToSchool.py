def solution(m, n, puddles):
    maps = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for p in puddles:
        maps[p[0]][p[1]] = -1
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if(row==1 and col==1):
                maps[1][1] = 1
                continue
            if (maps[row][col] == -1):
                maps[row][col] = 0
                continue
            maps[row][col] = maps[row][col - 1] + maps[row - 1][col]

    answer = maps[m][n] % 1000000007
    return answer


if __name__ == '__main__':
    m = 4
    n = 3
    puddles = [[2, 2]]
    sol = solution(m, n, puddles)
    print(sol)
