# Problem 11: String Validators
# HackerRank Link: https://www.hackerrank.com/challenges/string-validators/problem

s = input()
    
print(any(ch.isalnum() for ch in s))
print(any(ch.isalpha() for ch in s))
print(any(ch.isdigit() for ch in s))
print(any(ch.islower() for ch in s))
print(any(ch.isupper() for ch in s))
