# Problem 8: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem

n = int(raw_input())
integer_list = map(int, raw_input().split())

t = tuple(integer_list)
print(hash(t))
