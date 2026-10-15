# Problem 14: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
countries_list = set()

for i in range(n):
    country = input()
    countries_list.add(country)

print(len(countries_list))
