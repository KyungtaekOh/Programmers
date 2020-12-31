from collections import defaultdict


def solution(tickets):
    """
    1. 출발지 선택
    2. 사이클 검색
    3. 사이클의 순서 결정
    """
    answer = []
    mydict = defaultdict(set)
    ### Make Dictionary
    for i, j in tickets:
        mydict[i].add(j)

    def dfs(start, dict=mydict):

        return 0

    for i in mydict:
        for j in mydict[i]:
            answer = dfs(j)

    return answer


if __name__ == '__main__':
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    result = solution(tickets)
    print(result)
    # Expect : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
