def solution(lines):
    answer = 0
    history = []
    for line in lines:
        temp = line.split(" ")[1:]
        time = temp[0].split(":")
        end = int(time[0]) * 60 * 60 * 1000 + int(time[1]) * 60 * 1000 + float(time[2]) * 1000
        start = 1 + end - float(temp[1].replace('s', '')) * 1000
        history.append([int(start), int(end)])

    def isInvolve(start):
        end = start + 1000 - 1
        count = 0
        for s, e in history:
            if e >= start and s <= end:
                count += 1
        return count

    for st, et in history:
        answer = max([answer, isInvolve(st), isInvolve(et)])

    return answer
"""
Test case                           result
["2016-09-15 20:59:57.421 0.351s",  7
 "2016-09-15 20:59:58.233 1.181s", 
 "2016-09-15 20:59:58.299 0.8s", 
 "2016-09-15 20:59:58.688 1.041s", 
 "2016-09-15 20:59:59.591 2.412s", 
 "2016-09-15 21:00:00.464 1.466s", 
 "2016-09-15 21:00:00.741 1.581s", 
 "2016-09-15 21:00:00.748 2.31s", 
 "2016-09-15 21:00:00.966 0.381s", 
 "2016-09-15 21:00:02.066 2.62s"]
"""
