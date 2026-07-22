
import math

def file_read():
    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            pass

def first_star(gifts_got: int):
    for house in range(1, gifts_got, 1):
        elves = []
        gifts_delivered = 0

        for elf in range(1, int(math.sqrt(house)) + 1):
            if house % elf == 0:
                elves.append(elf)
                if elf != house // elf:
                    elves.append(house // elf)

        for elf in elves:
            gifts_delivered += (elf * 10)

        if gifts_delivered >= gifts_got:
            print("house num:", house)
            break

def second_star(gifts_got: int):
    for house in range(1, gifts_got, 1):
        elves = []
        gifts_delivered = 0

        for elf in range(1, int(math.sqrt(house)) + 1):
            if house % elf == 0:
                elves.append(elf)
                if elf != house // elf:
                    elves.append(house // elf)

        for elf in elves:
            if house <= (elf*50):
                gifts_delivered += (elf * 11)

        if house % 10000 == 0: #just to know it's alive, does not do any operation
            print(house)       #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        if gifts_delivered >= gifts_got:
            print("house num:", house)
            break

if __name__ == "__main__":
    GIFTS_GOT = 33100000

    #first_star(GIFTS_GOT)
    second_star(GIFTS_GOT)
