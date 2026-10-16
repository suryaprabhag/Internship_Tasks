# Problem 10: Swap Case
# HackerRank Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ""

    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
            
    return result

s = input()
result = swap_case(s)
print(result)
