
def file_read():
    moves = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            for char in line.strip():
                moves.append(char)
    return moves

def first_star(moves):
    houses_with_gifts = set()
    position = (0, 0)
    houses_with_gifts.add(position)

    for move in moves:
        position = get_movement(position, move)
        houses_with_gifts.add(position)

    print(f"houses with at least one gift = [{len(houses_with_gifts)}]")

def get_movement(position, move):
    x, y = position
    if move == '^':
        return (x, y + 1)
    if move == 'v':
        return (x, y - 1)
    if move == '>':
        return (x + 1, y)
    if move == '<':
        return (x - 1, y)
    return position

def second_star(moves):
    houses_with_gifts = set()

    santa_position = (0, 0)
    robosanta_position = (0, 0)

    houses_with_gifts.add(santa_position)

    santa_turn = True
    for move in moves:
        if santa_turn:
            santa_position = get_movement(santa_position, move)
            houses_with_gifts.add(santa_position)
        else:
            robosanta_position = get_movement(robosanta_position, move)
            houses_with_gifts.add(robosanta_position)

        santa_turn = not santa_turn # switch on/off

    print(f"houses with at least one gift = [{len(houses_with_gifts)}]")

if __name__ == "__main__":
    moves_list = file_read()

    #first_star(moves_list)
    second_star(moves_list)
