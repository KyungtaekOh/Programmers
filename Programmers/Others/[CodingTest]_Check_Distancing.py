def check(pl):
    for row in range(5):
        for col in range(5):
            if pl[row][col] != "P":
                continue
            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]: # [right, bottom, top, left] 순서
                pl[row][col] = "X"
                newr, newc = row + r, col + c
                if newr < 0 or newr > 4 or newc < 0 or newc > 4:
                    continue
                elif pl[newr][newc] == "X":
                    continue
                elif pl[newr][newc] == "P":
                    return 0
                else:       # "O"를 만난 경우(이동가능)
                    for rr, cc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        lastr, lastc = newr + rr, newc + cc
                        if lastr < 0 or lastr > 4 or lastc < 0 or lastc > 4:
                            continue
                        elif pl[lastr][lastc] == "P":
                            return 0
    else:
        return 1

def solution(places):
    answer = []
    for place in places:
        listp = [list(line) for line in place]  # String -> list
        answer.append(check(listp))
    return answer