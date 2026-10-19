# Problem 14: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    mid = n // 2

    first = s[:mid]
    second = s[mid:]

    count1 = Counter(first)
    count2 = Counter(second)

    changes = 0

    for char in count1:
        if count1[char] > count2[char]:
            changes += count1[char] - count2[char]

    return changes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
