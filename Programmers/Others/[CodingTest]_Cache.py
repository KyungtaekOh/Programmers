def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize==0:
        return len(cities)*5
    for cityname in cities:
        city = cityname.lower()
        if city in cache:
            idx = cache.index(city)
            temp = cache[idx]
            cache[idx:-1] = cache[idx+1:]
            cache[-1] = temp
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache[:-1] = cache[1:]
                cache[-1] = city
            else:
                cache.append(city)
            answer += 5
    return answer

"""
Test case
cahceSize   3
cities      ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
실행시간      50
"""