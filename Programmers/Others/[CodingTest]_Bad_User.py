from itertools import product
def solution(user_id, banned_id):
    ban_len = len(banned_id)
    answer, ban_list = [], [[] for i in range(ban_len)]
    for idx, ban in enumerate(banned_id):
        for user in user_id:
            if len(user) != len(ban): continue
            for u, b in zip(user, ban):
                if u != b and b != '*':break
            else:
                ban_list[idx].append(user)
    pd = list(product(*ban_list))
    for candi in pd:
        candiset = set(candi)
        if len(candiset) == ban_len and not candiset in answer:
            answer.append(candiset)
    return len(answer)


"""
Test case
user_id	                        banned_id	            result
["frodo", "fradi", "crodo",     ["fr*d*", "abc1**"]	    2
 "abc123", "frodoc"]	
["frodo", "fradi", "crodo",     ["*rodo", "*rodo",	    2
 "abc123", "frodoc"]	         "******"]
["frodo", "fradi", "crodo",     ["fr*d*", "*rodo", 	    3
 "abc123", "frodoc"]	         "******", "******"]
"""