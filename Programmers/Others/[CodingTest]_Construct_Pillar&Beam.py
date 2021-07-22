def check(build):
    for x, y, struct in build:
        if struct == 0:     # 기둥
            if not (y == 0 or (x, y-1, 0) in build or (x, y, 1) in build or (x-1, y, 1) in build):
                return False
        else:               # 보
            if not ((x, y-1, 0) in build or (x+1, y-1, 0) in build or (
                    (x-1, y, 1) in build and (x+1, y, 1) in build)):
                return False
    return True

def solution(n, build_frame):
    build = set()
    for x, y, struct, work in build_frame:
        if work:  # 설치
            if struct == 0:     # 기둥
                if y == 0 or (x, y-1, 0) in build or (x, y, 1) in build or (x-1, y, 1) in build:
                    build.add((x, y, struct))
            else:               # 보
                if (x, y-1, 0) in build or (x+1, y-1, 0) in build or ((x-1, y, 1) in build and (x+1, y, 1) in build):
                    build.add((x, y, struct))
        else:  # 삭제
            if struct == 0:     # 기둥
                build.remove((x, y, struct))
                if not check(build):
                    build.add((x, y, struct))
            else:               # 보
                build.remove((x, y, struct))
                if not check(build):
                    build.add((x, y, struct))
    answer = sorted(map(list, build), key=lambda k : (k[0], k[1], k[2]))
    return answer

"""
Test case
n               5
build_frame     [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
                 [2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
result          [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
"""