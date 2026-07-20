
def file_read():
    rows = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            rows.append(line.strip())

    return rows

def first_star(rows: list):
    literals_counter = 0
    in_memomry_counter = 0

    for row in rows:
        # literals
        literals_counter += len(row)

        # in memory
        row_memory = row[1:(len(row) - 1)]

        indexes = []

        skip_next = False
        for i, char in enumerate(row_memory):
            if skip_next:
                skip_next = False
                continue

            if char == "\\":
                indexes.append(i)
                skip_next = True

        print(indexes)

        new_row_memory = row_memory
        for i in indexes:
            symbol = row_memory[i + 1]

            if symbol == "x":
                new_row_memory = new_row_memory.replace(row_memory[i:(i + 4)], "_")

        new_row_memory = new_row_memory.replace("\\\\", "_")
        row_memory = new_row_memory.replace("\\", "")

        in_memomry_counter += len(row_memory)

        print(row, row_memory)

    print(literals_counter, in_memomry_counter, literals_counter - in_memomry_counter)

def second_star(rows: list):
    literals_counter = 0
    encoded_counter = 0

    for row in rows:
        # literals
        literals_counter += len(row)

        # encoded
        encoded_counter += len(row) + 2 # 2 are the initial and final quotation marks

        for char in row:
            if char in ["\\", "\""]:
                encoded_counter += 1

        print(row, literals_counter, encoded_counter)

    print(encoded_counter - literals_counter)

if __name__ == "__main__":
    ROWS = file_read()

    #first_star(ROWS)
    second_star(ROWS)
