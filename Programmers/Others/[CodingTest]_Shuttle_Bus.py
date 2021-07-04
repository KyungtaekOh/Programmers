def solution(n, t, m, timetable):
    for idx, time in enumerate(timetable):
        minute, second = time.split(':')
        timetable[idx] = int(minute) * 60 + int(second)
    table = sorted(timetable)
    mydict = [[540 + i * t, int(m), 0] for i in range(n)]
    tidx, didx = 0, 0
    while didx < n:
        if tidx == len(table):
            break
        if mydict[didx][1] > 0 and table[tidx] <= mydict[didx][0]:
            mydict[didx][2] = table[tidx]
            mydict[didx][1] -= 1
            tidx += 1
        else:
            didx += 1
    if mydict[-1][1] == 0:
        answer = mydict[-1][2] - 1
    else:
        answer = mydict[-1][0]
    return "%02d:%02d"%(answer//60, answer%60)


"""
Test case
n   t   m   timetable                                       answer
1	1	5	["08:00", "08:01", "08:02", "08:03"]	        "09:00"
2	10	2	["09:10", "09:09", "08:00"]	                    "09:09"
2	1	2	["09:00", "09:00", "09:00", "09:00"]	        "08:59"
1	1	5	["00:01", "00:01", "00:01", "00:01", "00:01"]	"00:00"
1	1	1	["23:59"]	                                    "09:00"
10	60	45  ["23:59","23:59", "23:59", "23:59", "23:59",    "18:00"
             "23:59", "23:59", "23:59", "23:59", "23:59", 
             "23:59", "23:59", "23:59", "23:59", "23:59", 
             "23:59"]
"""