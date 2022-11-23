'''
Author: 0xHamza
Subject: Nested List Reverse
Date: 23.11.2022
Source:
	-https://app.patika.dev/courses/python-temel/proje
    -https://stackabuse.com/python-how-to-flatten-list-of-lists/
'''

input = [[1, 2], [3, 4, [11,12]], [5, 6, 7]]
input.reverse()

print(input)
for i in range(len(input)):
    print("a")
    (input[i])=(input[i])[::-1]

print(input)
