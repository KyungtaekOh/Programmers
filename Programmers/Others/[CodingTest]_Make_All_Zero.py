"""
Greedy
"""
from collections import defaultdict, deque
def solution(a, edges):
    if sum(a) != 0: return -1
    answer = 0
    mdict = defaultdict(set)
    for s, e in edges:              # Tree의 형태 저장
        mdict[s].add(e)
        mdict[e].add(s)

    queue, visit = deque(), set()
    for k, v in mdict.items():      # LeafNode 찾기
        if len(v)==1:
            queue.append(k)

    while queue:                    # Leaf부터 Parent로 이동
        curr = queue.popleft()
        visit.add(curr)
        for node in mdict[curr]:
            if node not in visit:
                a[node] += a[curr]
                answer += abs(a[curr])
                mdict[node].remove(curr)    # Parent와 자신의 연결 삭제
                if len(mdict[node])==1:     # Parent가 Leaf가 되었을 때
                    queue.append(node)
    return answer

"""
Recursive
"""
import sys
sys.setrecursionlimit(300000)
def solution2(a, edges):
    if sum(a) != 0: return -1
    mdict = defaultdict(list)
    for s, e in edges:              # Tree의 형태 저장
        mdict[s].append(e)
        mdict[e].append(s)

    def dfs(curr=0, prev=0, answer=0):
        for node in mdict[curr]:
            if node != prev:        # Child로 재귀
                answer += dfs(node, curr)
        a[prev] += a[curr]
        answer += abs(a[curr])
        return answer

    return dfs()

"""
Test case
a	            edges	                    result
[-5,0,2,1,2]	[[0,1],[3,4],[2,3],[0,3]]	9
[0,1,0]	        [[0,1],[1,2]]	            -1
"""