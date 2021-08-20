def solution(phone_book):
    answer = True
    oneline = ""
    for row in range(len(phone_book)):
        oneline = oneline + "|" + phone_book[row]

    for col in range(len(phone_book)):
        if(oneline.count(phone_book[col]) > 1):
            front = oneline.find(phone_book[col])
            back = oneline.rfind(phone_book[col])
            if((oneline[front-1] == "|") and (oneline[back-1] == "|")):
                answer = False
                break
    return answer

"""
phone_book	                        return
["119", "97674223", "1195524421"]	false
["123","456","789"]	                true
["12","123","1235","567","88"]	    false
"""