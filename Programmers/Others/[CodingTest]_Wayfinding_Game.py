from collections import deque
def solution(nodeinfo):
    answer = [[], []]
    nodes = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(len(nodeinfo))]
    nodes = sorted(nodes, key=lambda k: (-k[1], k[0]))
    mdict = {}
    for x, y, idx in nodes:                 # Tree 만들기
        mdict[idx] = [x, y, None, None]
        curr = nodes[0][2]
        while True:
            if x > mdict[curr][0]:          # right child
                if mdict[curr][3] == None:  # child가 없으면 추가
                    mdict[curr][3] = idx
                    break
                curr = mdict[curr][3]
            elif x < mdict[curr][0]:        # left child
                if mdict[curr][2] == None:  # child가 없으면 추가
                    mdict[curr][2] = idx
                    break
                curr = mdict[curr][2]
            else:
                break

    for idx, order in enumerate([[3,2],[2,3]]): # 0:preorder, 1:postorder
        stack = [nodes[0][2]]                   # root node
        result = deque()
        while stack:
            curr = stack.pop()
            if idx == 0:
                result.append(curr)             # preorder 결과
            else:
                result.appendleft(curr)         # postorder 결과

            for child in order:                 # child 확인 순서
                if mdict[curr][child] != None:  # child가 없으면 추가
                    stack.append(mdict[curr][child])
        answer[idx] = list(result)
    return answer

"""
Test case
nodeinfo    [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result      [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
"""