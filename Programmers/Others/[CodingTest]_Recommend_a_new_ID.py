def solution(new_id):
    # 1,2단계
    new_id = ''.join([c if c.isalpha() or c.isdigit() or c=='-' or c=='_' or c=='.' else '' 
                      for i, c in enumerate(new_id.lower())])
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    new_id = new_id[1:] if new_id[0]=='.' and len(new_id)>1 else new_id
    new_id = new_id[:-1] if new_id[-1]=='.' else new_id
    # 5단계
    new_id = 'a' if len(new_id)==0 else new_id
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id[:-1] if new_id[-1]=='.' else new_id
    # 7단계
    answer = new_id+new_id[-1]*(3-len(new_id)) if len(new_id)<=2 else new_id
    return answer

"""
Test case
no	new_id	                        result
예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	                    "z--"
예3	"=.="	                        "aaa"
예4	"123_.def"	                    "123_.def"
예5	"abcdefghijklmn.p"	            "abcdefghijklmn"
"""