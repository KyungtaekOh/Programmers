def solution(record):
    answer = []
    userdict = {}
    for idx in range(len(record)):
        line = record[idx].split(" ")
        if line[0] != "Leave": userdict[line[1]] = line[2]
        if line[0] == "Change": continue
        answer.append(line[1] + ",님이 " + ''.join(["들어왔습니다." if line[0] == "Enter" else "나갔습니다."]))
    for idx, li in enumerate(answer):
        line = li.split(',')
        answer[idx] = userdict[line[0]] + line[1]
    return answer

"""
Test case
record                      result
["Enter uid1234 Muzi",      ["Prodo님이 들어왔습니다.",
 "Enter uid4567 Prodo",      "Ryan님이 들어왔습니다.",
 "Leave uid1234",            "Prodo님이 나갔습니다.",
 "Enter uid1234 Prodo",      "Prodo님이 들어왔습니다."]
 "Change uid4567 Ryan"]	   
"""