
def file_read():
    strings = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            strings.append(line.strip())

    return strings

def first_star(strings):
    nice_words_counter = 0

    for word in strings:
        if check(word):
            nice_words_counter += 1

    print(f"there is a total of [{nice_words_counter}] nice words")

def check(word):
    # at least 3 vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowels_counter = 0
    for char in word:
        if vowels_counter >= 3:
            break

        if char in vowels:
            vowels_counter += 1
    if vowels_counter < 3:
        return False

    # at least a double letter
    double_letter = False

    pre_char = word[0]
    for char in word[1:]:
        if char == pre_char:
            double_letter = True
            break
        pre_char = char
    if not double_letter:
        return False

    # not cointains an odd string
    odd_strings = ['ab', 'cd', 'pq', 'xy']

    for odd_string in odd_strings:
        if odd_string in word:
            return False

    return True

def second_star(strings):
    nice_words_counter = 0

    for word in strings:
        if better_check(word):
            nice_words_counter += 1

    print(f"there is a total of [{nice_words_counter}] nice words")

def better_check(word: str):
    # contains two letter pair
    possible_pairs = []

    for i, char in enumerate(word[1:]):
        possible_pairs.append(word[i] + char)

    max_divided_parts = 0

    for pair in possible_pairs:
        parts = word.split(pair)

        divided_parts = len(parts)

        if divided_parts > max_divided_parts:
            max_divided_parts = divided_parts

        if divided_parts >= 3:
            break

    if max_divided_parts < 3:
        return False

    # contains a repeated letter with a different letter between
    repeated_letter_around = False

    for i in range(0, (len(word) - 2), 1):
        char = word[i]
        two_next_char = word[i + 2]

        if char == two_next_char:
            repeated_letter_around = True
            break
    if not repeated_letter_around:
        return False

    return True


if __name__ == "__main__":
    STRINGS = file_read()

    #first_star(STRINGS)
    second_star(STRINGS)
