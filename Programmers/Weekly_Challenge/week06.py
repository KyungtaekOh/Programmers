def solution(weights, head2head):
    record = []
    for idx in range(len(weights)):
        win, lose = [0,0], 0
        for i, res in enumerate(head2head[idx]):
            if res == 'W':
                if weights[idx] < weights[i]:
                    win[0] += 1
                else:
                    win[1] += 1
            elif res == 'L':
                lose += 1
        if (sum(win)+lose) == 0:
            rate = 0
        else:
            rate = sum(win)/(sum(win)+lose)
        record.append([rate, win[0], weights[idx], idx+1])
    record = sorted(record, key=lambda k : [k[0], k[1], k[2], -k[3]], reverse=True)
    answer = [ele[-1] for ele in record]
    return answer

"""
Test case
weights	        head2head	                    result
[50,82,75,120]	["NLWL","WNLL","LWNW","WWLN"]	[3,4,1,2]
[145,92,86]	    ["NLW","WNL","LWN"]	            [2,3,1]
[60,70,60]	    ["NNN","NNN","NNN"]	            [2,1,3]
"""