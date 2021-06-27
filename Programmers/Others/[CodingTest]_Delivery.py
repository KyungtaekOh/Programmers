from collections import defaultdict
def solution(N, road, K):
    answer, mydict = {1:0}, defaultdict(set)
    for st, end, cost in road:
        mydict[st].add((end, cost))
        mydict[end].add((st, cost))
    def dfs(curr, total_c):
        if total_c > K:
            return
        for end, cost in mydict[curr]:
            if end in answer and total_c+cost >= answer[end]:
                continue
            elif total_c + cost <= K:
                answer[end] = total_c + cost
                dfs(end, total_c + cost)
    dfs(1, 0)
    return len(answer)

"""
Test case
N       Road                                K       Result
5       [[1,2,1],[2,3,3],[5,2,2],           3       4
        [1,4,2],[5,3,1],[5,4,2]]            
6       [[1,2,1],[1,3,2],[2,3,2],           4       4
        [3,4,3],[3,5,2],[3,5,3],[5,6,1]]
"""