def solution(play_time, adv_time, logs):
    if play_time == adv_time: return "00:00:00"
    pt, at = play_time.split(':'), adv_time.split(':')
    playtime = (int(pt[0]) * 3600) + (int(pt[1]) * 60) + (int(pt[2]))
    playlist = [0 for _ in range(playtime+1)]
    advtime = (int(at[0]) * 3600) + (int(at[1]) * 60) + (int(at[2]))

    for idx, line in enumerate(logs):   # 시청 시간 저장
        times = line.split('-')
        st, et = times[0].split(':'), times[1].split(':')
        start = (int(st[0]) * 3600) + (int(st[1]) * 60) + (int(st[2]))
        end = (int(et[0]) * 3600) + (int(et[1]) * 60) + (int(et[2]))
        playlist[start] += 1
        playlist[end] -= 1

    value = 0
    for idx in range(playtime+1):   # 시청자 수로 변경
        value += playlist[idx]
        playlist[idx] = value

    accum = sum(playlist[:advtime])
    candi, time = accum, 0          # 재생시간이 가장 많은 구간 탐색
    for remove, add in zip(range(playtime-advtime), range(advtime,playtime)):
        accum = accum-playlist[remove]+playlist[add]
        if candi < accum:
            candi = accum
            time = remove+1
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return '%02d:%02d:%02d'%(h, m, s)

"""
Test case
play_time   "02:03:55"
adv_time    "00:14:15"
logs        ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
result      "01:30:59"
"""