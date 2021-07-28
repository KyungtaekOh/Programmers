from collections import defaultdict
import re
def find_url(page, target):
    meta, link, count = [], [], 0
    for line in page:
        lowline = '-'+line.lower()+'-'
        meta.extend(re.findall('<meta property="og:url" content="\S+"', lowline))
        link.extend(re.findall('<a href="\S+"', lowline))
        text = ''
        for char in lowline:
            if char.isalpha():
                text += char
            else:
                if text == target:
                    count += 1
                text = ''
    return meta, link, count

def solution(word, pages):
    answer = 0
    pageinfo = defaultdict(list)    # url : [기본, 현재page의 링크, 현재page에 대한 링크, 링크점수]
    all_links = []
    for idx, page in enumerate(pages):
        lines = page.split('\n')
        meta, links, basic = find_url(lines, word.lower())
        url = meta[0][meta[0].find('t="')+3:-1]
        pageinfo[url] = [basic, len(links), []]
        for i in range(len(links)):
            all_links.append((url, links[i][links[i].find('f="')+3:-1]))

    for owner, target in all_links:         # 현재 page에 대한 링크 추가
        if target in pageinfo:
            pageinfo[target][2].append(owner)

    max_score = 0
    for idx, (k, v) in enumerate(pageinfo.items()): # 가장큰 매칭점수 찾기
        link_score = 0
        for link in v[2]:
            link_score += pageinfo[link][0] / pageinfo[link][1]
        match_score = pageinfo[k][0] + link_score
        if max_score < match_score:
            answer = idx
            max_score = match_score
    return answer
