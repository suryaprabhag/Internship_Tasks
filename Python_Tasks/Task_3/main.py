from solutions import (
    closest_to_zero,
    find_all_pairs,
    find_common_elements,
    max_consecutive_sum,
    move_zeros,
    rotate_list,
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    check_anagrams,
    first_repeating_character,
    second_highest,
    remove_duplicates,
    find_missing_number,
    find_two_sum,
)

sentence1 = "python is easy and python is powerful"
print(word_frequency(sentence1))

sentence2 = "Java Python Java SQL Python Java"
print(word_frequency(sentence2))


print(character_frequency("banana"))

print(character_frequency("programming"))


print(first_non_repeating_character("swiss"))

print(first_non_repeating_character("aabbcc"))


print(check_anagrams("listen", "silent"))

print(check_anagrams("hello", "world"))


print(first_repeating_character("programming"))

print(first_repeating_character("abcdef"))


print(move_zeros([0, 3, 0, 1, 2, 0, 4]))

print(move_zeros([1, 0, 2, 0, 3]))


print(second_highest([10, 20, 40, 30, 40, 20]))

print(second_highest([10, 20]))


print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))

print(remove_duplicates([1, 1, 2, 3, 2, 4]))


print(find_missing_number([1, 2, 4, 5, 6], 6))

print(find_missing_number([1, 3, 4, 5], 5))


print(find_two_sum([2, 7, 11, 15], 9))

print(find_two_sum([3, 2, 4], 6))



print(closest_to_zero([-8, -3, 2, 5, -2]))

print(closest_to_zero([-5, -1, 1, 4]))


print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

print(find_common_elements([4, 2, 4, 5, 2, 7], [2, 4, 7]))


print(rotate_list([1, 2, 3, 4, 5], 2))

print(rotate_list([10, 20, 30, 40], 1))


print(max_consecutive_sum([4, 7, 2, 9, 5]))

print(max_consecutive_sum([10, 20, 30, 40]))


print(find_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))

print(find_all_pairs([1, 2, 3, 4, 5], 6))