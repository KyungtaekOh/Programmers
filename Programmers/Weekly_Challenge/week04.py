def solution(table, languages, preference):
    answer, ldict = '', dict()
    for line in table:
        lsplit = line.split(' ')
        ldict[lsplit[0]] = dict()
        for idx, name in enumerate(lsplit[1:]):
            ldict[lsplit[0]][name] = 5 - idx

    result = 0
    for k, v in ldict.items():
        score = 0
        for idx, lang in enumerate(languages):
            if lang in v:
                score += preference[idx] * v[lang]
        if result < score:
            answer = k
            result = score
        elif result == score:
            answer = min(answer, k)

    return answer

"""
table       ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages   ["PYTHON", "C++", "SQL"]
preference  [7, 5, 5]
result      "HARDWARE"
"""