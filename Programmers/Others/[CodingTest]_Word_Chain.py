def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    else:
        return [0, 0]

"""
Test case
n	words	                                            result
3	["tank", "kick", "know", "wheel",                   [3,3]
     "land", "dream", "mother", "robot", "tank"]	
5	["hello", "observe", "effect", "take",              [0,0]
     "either", "recognize", "encourage", "ensure", 
     "establish", "hang", "gather", "refer", 
     "reference", "estimate", "executive"]	
2	["hello", "one", "even", "never",                   [1,3]
     "now", "world", "draw"]	
"""