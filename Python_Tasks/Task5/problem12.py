# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))


fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()
