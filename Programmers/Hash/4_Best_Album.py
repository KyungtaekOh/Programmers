def solution(genres, plays):
    answer, mdict = [], dict()
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in mdict:
            mdict[genre] = [play, []]
        else:
            mdict[genre][0] += play
        mdict[genre][1].append((idx, play))

    mdict = sorted(mdict.items(), key=lambda k: k[1][0], reverse=True)  # key를 기준으로 정렬
    for _, plist in mdict:
        plist = sorted(plist[1], key=lambda k: (-k[1], k[0]))   # play 내림차순, idx 오름차순 정렬
        answer += [idx[0] for idx in plist[:2]]
    return answer

"""
Test case
genres	                        plays	            return
["classic", "pop", "classic",   [500, 600, 150,	    [4, 1, 3, 0]
 "classic", "pop"]	            800, 2500]
"""