
def file_read():
    starting_number = ""

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            starting_number = line.strip()

    return starting_number

def solution(starting_number, times):
    value = starting_number

    for _ in range(times):
        next_value = ""

        if len(value) == 1:
            value = "1" + value
            continue

        previous = value[0]
        counter = 1

        for char in value[1:]:
            if char == previous:
                counter += 1
            else:
                next_value += str(counter) + previous

                previous = char
                counter = 1

        next_value += str(counter) + previous

        value = next_value

    print(len(value))

if __name__ == "__main__":
    STARTING_NUMBER = file_read()

    #first star
    solution(STARTING_NUMBER, 40)

    #second star
    solution(STARTING_NUMBER, 50)
