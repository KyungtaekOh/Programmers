import re
def solution(files):
    answer = [re.split(r"(\d+)", file) for file in files]
    answer.sort(key=lambda k : (k[0].lower(), int(k[1])))
    return [''.join(file) for file in answer]

"""
Test case
input   ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
output  ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

input   ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
output  ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
"""

