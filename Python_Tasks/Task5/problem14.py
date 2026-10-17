# Problem 14: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

result = sum(student_marks[query_name])/len(student_marks[query_name])

print(f"{result:.2f}")
