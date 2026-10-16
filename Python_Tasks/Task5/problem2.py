# Problem 1: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result

line = input()
result = split_and_join(line)
print(result)
