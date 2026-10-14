# Problem 12: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    heights = set(arr)
    return sum(heights)/len(heights)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)


