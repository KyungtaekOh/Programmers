import heapq
def solution(food_times, k):
    flen = len(food_times)
    if flen > k: return k+1
    queue = []
    for i, f in enumerate(food_times):
        heapq.heappush(queue, [f, i])

    prevfood, time = 0, 0
    for i in range(flen):
        qlen = len(queue)
        food, idx = queue[0]
        prevtime = time
        time += (food - prevfood) * qlen
        if time > k:
            queue.sort(key=lambda k : k[1])
            return queue[(k - prevtime) % qlen][1]+1
        heapq.heappop(queue)
        prevfood = food
    else:
        return -1

"""
Test case
food_times	k	result
[3, 1, 2]	5	1
"""