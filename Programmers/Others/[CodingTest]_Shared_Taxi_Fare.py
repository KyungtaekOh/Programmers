from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    answer = float('inf')
    mdict = defaultdict(dict)
    for src, dst, fare in fares:
        mdict[src][dst] = fare
        mdict[dst][src] = fare

    def dijkstra(start):
        distances = {node: float('inf') for node in mdict}
        distances[start] = 0
        queue = []
        heapq.heappush(queue, [distances[start], start])
        while queue:
            curr_dis, curr_dst = heapq.heappop(queue)
            if distances[curr_dst] < curr_dis:
                continue
            for new_dst, new_dis in mdict[curr_dst].items():
                dis = curr_dis + new_dis
                if dis < distances[new_dst]:
                    distances[new_dst] = dis
                    heapq.heappush(queue, [dis, new_dst])
        return distances

    for idx in range(1, n+1):
        if idx in mdict:
            answer = min(answer, dijkstra(s)[idx]+dijkstra(idx)[a]+dijkstra(idx)[b])

    return answer

"""
Test case
n	s	a	b	fares	                                result
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2],     82
                 [3, 1, 41], [5, 1, 24], [4, 6, 50],
                 [2, 4, 66], [2, 3, 22], [1, 6, 25]]	
"""
