def solution(skill, skill_trees):
    answer = 0
    for skill_t in skill_trees:
        flag, index = 0, 0
        for sk in skill_t:
            if index == len(skill):break
            if sk == skill[index]:
                index += 1
            elif sk in skill:
                flag = 1
                break
        if flag == 0:
            answer += 1
    return answer

'''
Test case
skill	skill_trees	                        return
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
'''