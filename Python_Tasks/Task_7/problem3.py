# Problem 3: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    count = 0
    expected = "SOS"

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            count += 1

    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
