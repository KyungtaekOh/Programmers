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

    def dfs2(word):
        visited = []
        stack = [word]
        while(stack):
            find = stack.pop()
            line = list(mydict[find])
            # while(line):



    ### BFS ###
    """
    2 try : while문을 돌며 stack에 쌓을 때 루프가 발생할 수 있음
    """
    def bfs(word):
        # stack
        # while에서 loop 발생 가능
        stack = set()
        depth = 0
        stack.add(depth)
        stack.add(word)
        while(stack):
            find = stack.pop()
            dic = list(mydict[find[1]])
            if target in dic:
                #여기서 반복문돌려서 최근숫자
                return
            for i in dic:
                stack.add([find[0] + 1, i])

    ### DFS ###
    """
    1 try : too many recursive depth
    이걸 중복되게 안하면 될거같은데..
    """
    def dfs(word):
        dic = list(mydict[word])
        if target in dic: return 0
        depth = 9999
        for i in dic:
            value = dfs(i)
            depth = min(depth, value)
        return depth + 1

    return dfs(begin)


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = solution(begin, target,words)
    print(result)