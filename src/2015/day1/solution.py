
def file_read():
    instructions = ''

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            instructions = line

    return instructions

def first_star(instructions):
    floor = 0

    for parenthesis in instructions:
        if parenthesis == "(":
            floor += 1
        elif parenthesis == ")":
            floor -= 1

    print(f"final floor = [{floor}]")

def second_star(instructions):
    floor = 0
    position = -1

    for i, parenthesis in enumerate(instructions):
        if parenthesis == "(":
            floor += 1
        elif parenthesis == ")":
            floor -= 1

        print(floor)

        if floor == -1:
            position = i + 1
            break

    print(f"entered basement at position = [{position}]")

if __name__ == "__main__":
    INSTRUCTIONS = file_read()

    #first_star(INSTRUCTIONS)
    second_star(INSTRUCTIONS)
