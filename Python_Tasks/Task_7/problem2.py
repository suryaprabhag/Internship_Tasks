# Problem 2: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))

frequency = Counter(rooms)

for room, count in frequency.items():
    if count == 1:
        print(room)
        break
