# Problem 15: Set .difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
set_n = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

diff_set = set_n - set_b
print(len(diff_set))
