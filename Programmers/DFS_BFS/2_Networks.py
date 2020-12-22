def solution(n, coms):
    answer = 0
    for a in range(n):  # n번째 행으로 새로운 네트워크를 시작
        if (coms[a][a] != -1):
            answer += 1
            net = [a]
            while (len(net) != 0):  # n개의 행을 반복
                line = net.pop(0)
                if (coms[line][line] == 1):
                    coms[line][line] = -1
                    for i in range(n):  # n개의 열을 반복하여 넷웤 찾기
                        if (coms[line][i] == 1):
                            net.append(i)
        else:
            continue
    return answer


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0],
                 [1, 1, 0],
                 [0, 0, 1]]
    sol = solution(n, computers)
    print(sol)