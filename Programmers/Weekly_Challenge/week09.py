from collections import defaultdict, deque
def solution(n, wires):
    answer = float('inf')
    mdict = defaultdict(list)
    for s, e in wires:
        mdict[s].append(e)
        mdict[e].append(s)
    for s, e in wires:
        queue = deque([1])
        visit = set()
        while queue:
            curr = queue.popleft()
            if curr in visit:
                continue
            else:
                visit.add(curr)
            for node in mdict[curr]:
                if (curr == s and node == e) or (curr == e and node == s):
                    continue
                queue.append(node)
        diff = abs(n - (len(visit) * 2))
        answer = min(diff, answer)

    return answer

"""
Test case
n	wires	                                            result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	                                0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1
"""