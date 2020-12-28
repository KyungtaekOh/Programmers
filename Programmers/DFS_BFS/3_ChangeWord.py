"""
First solve : 2020-12-28
"""
from collections import defaultdict

def solution(begin, target, words):
    if not (target in words): return 0  # words에 없을 경우

    length = len(words)
    mydict = defaultdict(set)

    ### Make dictionary ###
    for i in range(length + 1):  # i번째 단어로 검색
        if (i == length):
            find = begin
        else:
            find = words[i]
        for j in range(length):  # j번째 단어로 비교
            if (i == j): continue
            diff = 0
            for a in range(len(words[j])):  # 단어비교
                if diff < 2:
                    if find[a] != words[j][a]:
                        diff += 1
                        continue
                else:
                    break
            if (diff == 1):
                mydict[find].add(words[j])

    def bfs(word):
        visited = set()
        queue = [word]
        level = 0
        while(True):
            q_len = len(queue)
            for j in range(q_len):
                find = queue.pop(0)
                visited.add(find)
                line = list(mydict[find])
                for i in line:
                    if not (i in visited):
                        queue.append(i)
                    if(i == target):
                        return level + 1
            level += 1

    return bfs(begin)
"""
Frist solve
    try 1 : DFS 에서 too many recursive depth
    try 2 : BFS 에서 cycle이 생성될 수 있음을 인지
    try 3 : mydict의 형태가 결국 tree가 아닌 graph임을 인지
            -> 출발점이 있는 graph이므로 BFS를 통해 level단위 검색
            -> graph의 형태이므로 visited를 통해 cycle 방지
"""

if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "hor", "tor", "tog", "cog"]
    result = solution(begin, target, words)
    print(result)