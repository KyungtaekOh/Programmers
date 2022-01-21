def solution(info, edges):
    mdict = {}
    for idx, io in enumerate(info):     # 트리 만들기
        mdict[idx] = []
    for s, e in edges:
        mdict[s].append(e)

    def search(curr, maxs, sheep, wolf, nexts):     # DFS
        sheep += info[curr] ^ 1
        wolf += info[curr]
        if sheep <= wolf: return 0
        maxs = max(maxs, sheep)

        nexts = mdict[curr] + nexts
        for idx, ele in enumerate(nexts):           # 다음으로 방문할 노드
            result = search(ele, maxs, sheep, wolf, nexts[:idx]+nexts[idx+1:])
            maxs = max(maxs, result)
        return maxs

    return search(0, 0, 0, 0, [])

"""
Test case
info	                    edges	                                result
[0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],               5
                             [8,7],[9,10],[9,11],[4,3],
                             [6,5],[4,6],[8,9]]	
[0,1,0,1,1,0,1,0,0,1,0]	    [[0,1],[0,2],[1,3],[1,4],               5
                             [2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	
"""
