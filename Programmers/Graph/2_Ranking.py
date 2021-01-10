"""
First solve : 2021-01-10
"""
def solution(n, results):
    answer = 0
    score = [[0]*n for i in range(n)]
    win = [[] for i in range(n+1)]
    lose = [[] for i in range(n+1)]

    for w, l in results:    # win:1 lose:2
        score[w-1][l-1] = 1
        score[l-1][w-1] = 2
        win[w].append(l)
        lose[l].append(w)

    def bfs(now, find=1, visited=set()):
        w = []

        if (find == 1):temp = win[now]
        else: temp = lose[now]

        if (now in visited): return temp
        else: visited.add(now)

        for i in temp:
            w += bfs(i, find, visited)
        w += temp
        w = list(set(w))
        for i in w:
            score[now-1][i-1] = find
        return w

    for i in range(1, n+1):
        nset = set()
        bfs(i, 1, nset)
        nset.clear()
        bfs(i, 2, nset)
        if(score[i-1].count(0) == 1):
            answer += 1
    return answer

if __name__ == '__main__':
    # n = 7
    # results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [2, 6], [6, 5], [5, 7]]

    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    sol = solution(n, results)
    print("answer:", sol)