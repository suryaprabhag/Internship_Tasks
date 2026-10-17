# Problem 16: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))

stock = Counter(shoe_sizes)

customers = int(input())
total_earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if stock[size] > 0:
        total_earnings += price
        stock[size] -= 1

print(total_earnings)
