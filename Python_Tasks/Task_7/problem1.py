# Problem 1: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

english_students = int(input())
english_students_set = set(map(int,input().split()))
french_students = int(input())
french_students_set = set(map(int,input().split()))
result = english_students_set^french_students_set

print(len(result))
