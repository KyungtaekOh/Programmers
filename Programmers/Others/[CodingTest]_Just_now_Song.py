def solution(m, musicinfos):
    candidate = []
    for i, info in enumerate(musicinfos):
        start, end, title, music = info.split(',')
        sh, sm = start.split(':')
        eh, em = end.split(':')
        ptime = (int(eh)*60+int(em))-(int(sh)*60+int(sm))
        prange = ''
        idx, mlen = 0, 0
        while mlen<ptime:           # 연주된 전체 음들 구하기
            prange += music[idx]
            idx = (idx+1)%len(music)
            if music[idx] == '#':
                prange += music[idx]
                idx = (idx+1)%len(music)
            mlen += 1
        prange += '-'
        while len(m) < len(prange): # m과 같은 멜로디가 있는지 검색
            check = prange.find(m)
            heard = len(m)
            if check != -1 and prange[check+heard] != '#':
                candidate.append([ptime, i, title])
                break
            else:
                prange = prange[check+heard:]
    candidate.sort(key=lambda k:(k[0], -k[1]), reverse=True)
    if len(candidate)==0:
        return "(None)"
    return candidate[0][2]

"""
Test case
m	        musicinfos	                                                answer
"ABCDEFG"	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
"ABC"	    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"
"""
