# Q1. Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Q2. Find the Frequency of Each Character in a Word

def character_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Q3. Find the First Non-Repeating Character in a Word

def first_non_repeating_character(word):
    frequency = {}

    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    for char in word:
        if frequency[char] == 1:
            return char

    return None

# Q4. Check Whether Two Strings Are Anagrams

def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    frequency1 = {}
    frequency2 = {}

    for char in s1:
        frequency1[char] = frequency1.get(char, 0) + 1

    for char in s2:
        frequency2[char] = frequency2.get(char, 0) + 1

    return frequency1 == frequency2


# Q5. Find the First Repeating Character in a String

def first_repeating_character(word):
    seen = set()

    for char in word:
        if char in seen:
            return char

        seen.add(char)

    return None


# Q6. Move All Zeros to the End of a List

def move_zeros(numbers):
    result = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    result.extend([0] * zero_count)

    return result

# Q7. Find the Second Highest Distinct Number in a List

def second_highest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result


# Q9. Find the Missing Number from 1 to N

def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target

def find_two_sum(nums, target):
    seen = {}

    for num in nums:
        complement = target - num

        if complement in seen:
            return [complement, num]

        if num not in seen:
            seen[num] = True

    return []


# Q11. Find the Number Closest to Zero

def closest_to_zero(numbers):
    if not numbers:
        return None

    closest = numbers[0]

    for num in numbers:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest


# Q12. Find Common Elements Between Two Lists

def find_common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


# Q13. Rotate a List to the Right by K Positions

def rotate_list(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(numbers):
    max_sum = numbers[0] + numbers[1]

    for i in range(1, len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def find_all_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pair = tuple(sorted([num, complement]))
            pairs.add(pair)

        seen.add(num)

    return [list(pair) for pair in sorted(pairs)]