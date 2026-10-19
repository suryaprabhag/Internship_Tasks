# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alphabets = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        index = abs(i)

        left = alphabets[size - 1:index:-1]
        right = alphabets[index:size]

        row = "-".join(left + right)

        print(row.center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
