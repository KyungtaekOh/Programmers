"""
First solve : 2021-01-08
"""
def solution(n, edge):
    answer = 0
    mydict = [[] for i in range(n)]
    for i, j in edge:              # 경로 저장
        mydict[i - 1].append(j)
        mydict[j - 1].append(i)

    queue = [1]
    visited = [1] + [0 for i in range(n - 1)]
    while (queue):                  # BFS
        answer = len(queue)
        for i in range(answer):
            node = queue.pop(0)
            for a in mydict[node - 1]:
                if visited[a - 1] == 0:
                    queue.append(a)
                    visited[a - 1] = 1
    return answer


if __name__ == '__main__':
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    result = solution(n, vertex)
    print(result)
    # Expect : 3
