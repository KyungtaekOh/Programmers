from collections import defaultdict, deque
def solution(enroll, referral, seller, amount):
    endict = defaultdict()		# 자신:추천인을 담을 dict
    for en, ref in zip(enroll, referral):   # 자신의 추천인을 dict에 저장
        endict[en] = [ref, 0]
    for name, num in zip(seller, amount):   # 판매자, 판매금액
        queue = deque([[name, num*100]])
        while queue:
            na, pr = queue.popleft()        # 이름, 금액
            if na == '-':break
            tenp = int(pr*0.1)	# 10%의 금액
            if tenp >= 1:       # 1원보다 크면 90%를 갖고 10%를 queue에 추가
                endict[na][1] += pr-tenp
                queue.append([endict[na][0], tenp])
            else:		# 1보다 작으면 전부갖고 queue에 아무것도 넣지않음
                endict[na][1] += pr
    return [earn[1] for earn in endict.values()]

"""
enroll      ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller      ["young", "john", "tod", "emily", "mary"]
amount      [12, 4, 2, 5, 10]

result      [360, 958, 108, 0, 450, 18, 180, 1080]
"""