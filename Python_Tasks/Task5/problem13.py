# Problem 13: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem


students = []

n = int(input())

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

unique_scores = sorted(set(student[1] for student in students))

second_lowest = unique_scores[1]

names = []

for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

for name in sorted(names):
    print(name)
