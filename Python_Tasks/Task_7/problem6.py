# Problem 6: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    characters = set(s.lower())

    if alphabets.issubset(characters):
        return "pangram"
    else:
        return "not pangram"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
