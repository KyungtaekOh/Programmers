from collections import defaultdict
def solution(k, room_number):
    answer = []
    rdict = defaultdict()   # [first, num]
    for num in room_number:
        if num in rdict:    # 찾아서 넣는 경우
            first = num
            while True:
                if rdict[first][0] == False:
                    first = rdict[first][1]
                else:
                    break
            temp = rdict[first][1]
            if temp+1 in rdict and rdict[temp+1][0]==True:
                rdict[temp] = [False, first]
                rdict[first][1] = rdict[temp+1][1]
                rdict[temp+1] = [False, first]
            else:
                rdict[temp] = [False, first]
                rdict[first][1] = temp+1
            room = temp
        else:               # 그냥 넣어도 되는 경우
            if num+1 in rdict:
                rdict[num] = [True, rdict[num+1][1]]
                rdict[num+1] = [False, num]
            else:
                rdict[num] = [True, num+1]
            if num-1 in rdict:
                first = num-1
                while True:
                    if rdict[first][0] == False:
                        first = rdict[first][1]
                    else:
                        break
                rdict[first][1] = rdict[num][1]
                rdict[num] = [False, first]
            room = num
        answer.append(room)
    return answer

def solution2(k, room_number):
    answer = []
    rdict = defaultdict()
    for num in room_number:
        idx = num
        visit = {idx}
        while idx in rdict:
            idx = rdict[idx]
            visit.add(idx)
        for room in visit:
            rdict[room] = idx+1
        answer.append(idx)
    return answer

"""
Test case
k	room_number	    result
10	[1,3,4,1,3,1]	[1,3,4,2,5,6]
"""