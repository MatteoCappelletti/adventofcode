
def file_read():
    ticket = {}
    with open("./input_ticket.txt", 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(":")

            ticket[parts[0].strip()] = int(parts[1])

    aunts = []
    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:

            div_i = -1
            for i, char in enumerate(line):
                if char == ":":
                    div_i = i
                    break

            aunt_id = int(line[:div_i].split()[1])

            infos = {}

            parts = line[(div_i + 1):].split(",")

            for part in parts:
                key, value = part.split(":")
                infos[key.strip()] = int(value.strip())

            aunts.append((aunt_id, infos))

    return ticket, aunts

def first_star(ticket, aunts):

    for aunt_id, infos in aunts:
        is_all_matched = True

        for key, value in infos.items():

            if ticket[key] != value:
                is_all_matched = False
                break

        if is_all_matched:
            print(aunt_id, infos)

def second_star(ticket, aunts):
    to_be_greater = ["cats", "trees"]
    to_be_fewer = ["pomeranians", "goldfish"]

    for aunt_id, infos in aunts:
        is_all_matched = True

        for key, value in infos.items():

            if key in to_be_greater:
                if ticket[key] >= value:
                    is_all_matched = False
                    break

            elif key in to_be_fewer:
                if ticket[key] <= value:
                    is_all_matched = False
                    break

            else:
                if ticket[key] != value:
                    is_all_matched = False
                    break

        if is_all_matched:
            print(aunt_id, infos)

if __name__ == "__main__":
    TICKET, AUNTS = file_read()

    #first_star(TICKET, AUNTS)
    second_star(TICKET, AUNTS)
