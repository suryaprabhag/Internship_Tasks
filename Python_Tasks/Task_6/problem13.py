# Problem 13: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

common_set = set_n | set_b
print(len(common_set))
