# Problem 4: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    reversed_s = s[::-1]

    for i in range(1, len(s)):
        original_diff = abs(ord(s[i]) - ord(s[i - 1]))
        reverse_diff = abs(ord(reversed_s[i]) - ord(reversed_s[i - 1]))

        if original_diff != reverse_diff:
            return "Not Funny"

    return "Funny"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
