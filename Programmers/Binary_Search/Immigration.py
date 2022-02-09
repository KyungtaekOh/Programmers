def solution(n, times):
    answer = 0
    mint, maxt = min(times), n*max(times)
    while mint<=maxt:
        mid = (mint+maxt)//2    # 기준 시간

        count = 0               # 기준 시간에서 심사가능한 사람 수
        for time in times:
            count += mid//time

        if n<=count:            # 심사가능 사람수가 n보다 많을 때
            answer = mid
            maxt = mid-1
        else:                   # 심사가능 사람수가 n보다 적을 때
            mint = mid+1
    return answer

"""
Test case
n	times	    return
6	[7, 10]	    28
"""