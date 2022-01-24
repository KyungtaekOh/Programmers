max_score, candi = 0, []
def cal_score(info, board):         # 점수차 계산
    iscore, bscore = 0, 0
    for idx, (iele, bele) in enumerate(zip(info, board)):
        if iele==0 and bele==0: continue
        if iele<bele:
            bscore += (10-idx)
        else:
            iscore += (10-idx)
    return bscore-iscore

def search(index, arrow, info, board):      # DFS
    global max_score, candi
    if index == 11:
        if arrow > 0: board[-1]=arrow           # 남은 화살을 0점에 쏘는 것
        diff = cal_score(info, board)
        if diff<=0:return
        if diff > max_score:
            max_score = diff
            candi = [[ele for ele in board]]
        elif diff == max_score:
            candi.append([ele for ele in board])
        return
    for_hit = info[index]
    board[index] = 0
    search(index + 1, arrow, info, board)       # 맞추지 않았을 경우
    if for_hit < arrow:                         # 맞추었을 경우
        board[index] = for_hit+1
        search(index+1, arrow-(for_hit+1), info, board)


def solution(n, info):
    global max_score, candi
    search(0, n, info, [0 for i in info])   # DFS
    if not candi:       # 우승할 수 없는 경우
        return [-1]
    else:               # 우승할 경우
        candi.sort(key = lambda k:k[::-1], reverse=True)
    return candi[0]

"""
Test case
n	info	                result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
"""