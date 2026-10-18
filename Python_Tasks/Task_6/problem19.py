# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()

    frequency = Counter(s)

    result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)
