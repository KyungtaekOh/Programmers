from collections import defaultdict
def search(head, query):    # query는 '?'가 suffix의 위치로만 입력
    curr = head
    result = 0
    for char in query:
        if char == '?':     # '?'를 만나면 뒤의 모든 경우가 가능
            return result
        else:
            if char not in curr[0]:     # 가능한 단어가 없는 경우
                return 0
            result = curr[0][char][1]
            curr = curr[0][char]
    return result

def solution(words, queries):
    answer = []
    prefix, suffix = defaultdict(), defaultdict()
    for word in words:              # Trie 생성
        wlen = len(word)
        if wlen not in prefix:      # key값이 없을 때 추가
            prefix[wlen], suffix[wlen] = [{}, 0], [{}, 0]
        for dictionary, string in [[prefix, word], [suffix, word[::-1]]]:
            curr = dictionary[wlen]
            curr[1] += 1
            for char in string:     # Trie 형태로 word 추가
                if char not in curr[0]:
                    curr[0][char] = [{}, 0]
                curr[0][char][1] += 1
                curr = curr[0][char]

    for query in queries:       # 검색
        qlen = len(query)
        if qlen not in prefix:  # 길이가 맞지 않는 경우
            answer.append(0)
        elif query[0]=='?' and query[-1]=='?':  # 전부 '?'
            answer.append(prefix[qlen][1])
        elif query[0]=='?':     # suffix
            answer.append(search(suffix[qlen], query[::-1]))
        elif query[-1]=='?':    # prefix
            answer.append(search(prefix[qlen], query))

    return answer

"""
Test case
words   ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries ["fro??", "????o", "fr???", "fro???", "pro?"]
result  [3, 2, 4, 1, 0]
"""