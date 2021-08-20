def solution(participant, completion):
    participant.sort()
    completion.sort()
    maxNum = len(completion)
    answer = ''

    for i in range(maxNum):
        if (i == maxNum - 1):
            answer = participant[i + 1]
        if (participant[i] == completion[i]):
            continue
        else:
            return participant[i]

    return answer

"""
Test case
participant	                                        completion	                                return
["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                        "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"
"""