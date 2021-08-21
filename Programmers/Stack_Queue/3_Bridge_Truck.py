def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length
    while queue:
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
        answer += 1
    return answer

"""
Test case
bridge_length	weight	truck_weights	                    return
2	            10	    [7,4,5,6]	                        8
100	            100	    [10]	                            101
100	            100	    [10,10,10,10,10,10,10,10,10,10]	    110

"""