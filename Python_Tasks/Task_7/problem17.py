# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    if s[0] == '0':
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        num = first
        result = ""

        while len(result) < len(s):
            result += str(num)
            num += 1

        if result == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
