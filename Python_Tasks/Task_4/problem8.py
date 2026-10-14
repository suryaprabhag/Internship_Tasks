# Problem 8: What's Your Name?
# HackerRank Link: https://www.hackerrank.com/challenges/whats-your-name/problem

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

first_name = input()
last_name = input()
print_full_name(first_name, last_name)
