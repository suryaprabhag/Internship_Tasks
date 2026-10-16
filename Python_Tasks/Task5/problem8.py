# Problem 8: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
countries = set()

for i in range(1,n+1):
    country = input()
    countries.add(country)
    
print(len(countries))
