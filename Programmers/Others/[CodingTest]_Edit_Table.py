from collections import deque
class node():
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    p = node(0)
    curr = p
    for idx in range(1, n):     # linked list 생성
        newnode = node(idx)
        newnode.prev = p
        p.next = newnode
        p = newnode
        if idx == k+1:      # 시작지점 Node
            curr = p.prev
    stack = deque()         # 삭제를 저장할 stack
    for c in cmd:
        if c[0] == "D":
            for i in range(int(c[2:])):
                curr = curr.next
        elif c[0] == "U":
            for i in range(int(c[2:])):
                curr = curr.prev
        elif c[0] == "C":       # 삭제 명령어
            stack.appendleft(curr)
            answer[curr.value] = "X"
            if curr.next == None:       # 마지막 node일 경우
                curr.prev.next = None
                curr = curr.prev
            elif curr.prev == None:     # 처음 node일 경우
                curr.next.prev = None
                curr = curr.next
            else:                       # 중간 node일 경우
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = curr.next
        elif c[0] == "Z":       # 복구 명령어
            latest = stack.popleft()
            answer[latest.value] = "O"
            if latest.next == None:     # 마지막 node일 경우
                latest.prev.next = latest
            elif latest.prev == None:   # 처음 node일 경우
                latest.next.prev = latest
            else:                       # 중간 node일 경우
                latest.next.prev = latest
                latest.prev.next = latest
    return "".join(answer)

"""
Test case
n	k	cmd	                            result
8	2	["D 2","C","U 3","C","D 4",     "OOOOXOOO"
         "C","U 2","Z","Z"]	
8	2	["D 2","C","U 3","C","D 4",     "OOXOXOOO"
         "C","U 2","Z","Z","U 1","C"]	
"""