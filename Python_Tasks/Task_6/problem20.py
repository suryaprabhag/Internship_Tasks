# Problem 20: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

for _ in range(n):
    mobile = input().strip()

    if re.fullmatch(r'[789][0-9]{9}', mobile):
        print("YES")
    else:
        print("NO")
