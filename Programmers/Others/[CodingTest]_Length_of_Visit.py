def solution(dirs):
    direc = {'U':(0,1), 'D':(0,-1), 'R':(1,0), "L":(-1,0)}
    visit = set()
    x, y = 0, 0
    for d in dirs:
        nx, ny = x+direc[d][0], y+direc[d][1]
        if -5<=nx<=5 and -5<=ny<=5:
            continue
        if not (((x,y), (nx, ny)) in visit or ((nx,ny), (x,y)) in visit):
            visit.add(((x,y), (nx, ny)))
        x, y = nx, ny
    return len(visit)

"""
Test case
dirs	        answer
"ULURRDLLU"	    7
"LULLLLLLU"	    7
"""