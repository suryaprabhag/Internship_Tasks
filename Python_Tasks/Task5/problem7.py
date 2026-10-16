# Problem 7: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

result = sorted(set1.symmetric_difference(set2))

for num in result:
    print(num)
