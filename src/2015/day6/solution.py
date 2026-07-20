
def file_read():
    instructions = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            father_parts = line.strip().split("through")

            x2, y2 = father_parts[1].strip().split(",")
            final_coordinates = (int(x2), int(y2))

            action = ""
            if "turn on" in father_parts[0]:
                action = "turn on"
            elif "turn off" in father_parts[0]:
                action = "turn off"
            elif "toggle" in father_parts[0]:
                action = "toggle"

            clear_first_father_part = father_parts[0].replace("turn on","").replace("turn off","").replace("toggle","")
            x1, y1 = clear_first_father_part.strip().split(",")
            initial_coordinates = (int(x1), int(y1))

            instructions.append((action, initial_coordinates, final_coordinates))

    return instructions

def first_star(instructions):
    grid = []

    for _ in range(1000):
        row = []
        for _ in range(1000):
            row.append(False)
        grid.append(row)

    for action, (init_x, init_y), (final_x, final_y) in instructions:
        for x in range(init_x, final_x + 1, 1):
            for y in range(init_y, final_y + 1, 1):

                if action == "turn on":
                    grid[x][y] = True
                elif action == "turn off":
                    grid[x][y] = False
                elif action == "toggle":
                    grid[x][y] = not grid[x][y]

    lights_on_counter = 0

    for row in grid:
        for light in row:
            if light:
                lights_on_counter += 1

    print(f"there are [{lights_on_counter}] lights turned on")


def second_star(instructions):
    grid = []

    for _ in range(1000):
        row = []
        for _ in range(1000):
            row.append(0)
        grid.append(row)

    for action, (init_x, init_y), (final_x, final_y) in instructions:
        for x in range(init_x, final_x + 1, 1):
            for y in range(init_y, final_y + 1, 1):

                if action == "turn on":
                    grid[x][y] += 1
                elif action == "turn off":
                    if grid[x][y] > 0:
                        grid[x][y] -= 1
                elif action == "toggle":
                    grid[x][y] += 2

    brightness = 0

    for row in grid:
        for light in row:
            brightness += light

    print(f"the total brightness is [{brightness}]")

if __name__ == "__main__":
    INSTRUCTIONS = file_read()

    #first_star(INSTRUCTIONS)
    second_star(INSTRUCTIONS)
