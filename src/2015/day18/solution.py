
def file_read():
    grid = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char.strip())
            grid.append(row)

    return grid

def first_star(grid: list, steps: int):
    using_grid = grid

    for _ in range(steps):
        #print_map(using_grid, -1, -1)

        altered_grid = []

        for x, row in enumerate(using_grid):
            altered_row = []

            for y, _ in enumerate(row):

                if check_light(using_grid, x, y):
                    altered_row.append("#")
                else:
                    altered_row.append(".")

            altered_grid.append(altered_row)

        using_grid = altered_grid

    #print_map(using_grid, -1, -1)

    print("lights on:", lights_on_counter(using_grid))

def check_light(grid, x, y):
    #print_map(grid, x, y)

    lights_on = 0
    light = grid[x][y]

    min_x = 0
    max_x = len(grid) - 1

    min_y = 0
    max_y = len(grid[0]) - 1

    has_top = True if x > min_x else False
    has_bottom = True if x < max_x else False
    has_left = True if y > min_y else False
    has_right = True if y < max_y else False

    if has_top and grid[x - 1][y] == "#":
        lights_on += 1
    if has_bottom and grid[x + 1][y] == "#":
        lights_on += 1
    if has_left and grid[x][y - 1] == "#":
        lights_on += 1
    if has_right and grid[x][y + 1] == "#":
        lights_on += 1

    if has_top and has_left and grid[x - 1][y - 1] == "#":
        lights_on += 1
    if has_top and has_right and grid[x - 1][y + 1] == "#":
        lights_on += 1
    if has_bottom and has_left and grid[x + 1][y - 1] == "#":
        lights_on += 1
    if has_bottom and has_right and grid[x + 1][y + 1] == "#":
        lights_on += 1

    if light == "#" and lights_on in [2, 3]:
        return True
    if light == "." and lights_on in [3]:
        return True

    return False

def lights_on_counter(grid):
    total = 0
    for row in grid:
        for char in row:
            if char == "#":
                total += 1
    return total

def print_map(grid, cell_x, cell_y):
    print(f"\ncell [{cell_x}][{cell_y}]")
    for x, row in enumerate(grid):
        row_print = ""
        for y, char in enumerate(row):
            if x == cell_x and y == cell_y:
                row_print += "X"
                continue

            row_print += char
        print(row_print)

def second_star(grid, steps):
    using_grid = grid

    corners = [(0, 0), (0, (len(grid[0]) - 1)), ((len(grid) - 1), 0), ((len(grid) - 1), (len(grid[0]) - 1))]

    for x, y in corners:
        using_grid[x][y] = "#"

    for _ in range(steps):
        #print_map(using_grid, -1, -1)

        altered_grid = []

        for x, row in enumerate(using_grid):
            altered_row = []

            for y, _ in enumerate(row):
                if (x, y) in corners:
                    altered_row.append("#")
                    continue

                if check_light(using_grid, x, y):
                    altered_row.append("#")
                else:
                    altered_row.append(".")

            altered_grid.append(altered_row)

        using_grid = altered_grid

    #print_map(using_grid, -1, -1)

    print("lights on:", lights_on_counter(using_grid))

if __name__ == "__main__":
    GRID = file_read()
    STEPS = 100

    #first_star(GRID, STEPS)
    second_star(GRID, STEPS)
