
def file_read():
    tanks = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            tanks.append(int(line.strip()))

    return tanks

def first_star(tanks, liters_to_fit):

    combinations = tanks_filler(tanks, liters_to_fit)

    print("combinations:", combinations)

def tanks_filler(avaible_tanks, remaining_liters):
    combinations = 0

    if remaining_liters == 0:
        return 1

    if len(avaible_tanks) == 0:
        return 0

    if min(avaible_tanks) > remaining_liters:
        return 0

    for i, tank in enumerate(avaible_tanks):
        if remaining_liters < tank:
            continue

        combinations += tanks_filler(avaible_tanks[(i+1):], (remaining_liters - tank))

    return combinations

def second_star(tanks, liters_to_fit):
    min_tank_used = min_tanks_needed_finder(tanks, liters_to_fit, 0, 1_000_000)

    result = min_tanks_filler(tanks, liters_to_fit, 0, min_tank_used)

    print(f"tank used: [{min_tank_used}] | combinations: [{result}]")

def min_tanks_needed_finder(avaible_tanks, remaining_liters, tanks_used, min_tanks_used):
    if remaining_liters == 0:
        return tanks_used

    if len(avaible_tanks) == 0:
        return 1_000_000

    if min(avaible_tanks) > remaining_liters:
        return 1_000_000

    for i, tank in enumerate(avaible_tanks):
        if remaining_liters < tank:
            continue

        new_tank_used=min_tanks_needed_finder(avaible_tanks[(i+1):],(remaining_liters-tank),tanks_used+1,min_tanks_used)
        min_tanks_used = min(min_tanks_used, new_tank_used)

    return min_tanks_used

def min_tanks_filler(avaible_tanks, remaining_liters, tank_used, max_avaible_tanks):
    combinations = 0

    if tank_used > max_avaible_tanks:
        return 0

    if remaining_liters == 0:
        return 1

    if len(avaible_tanks) == 0:
        return 0

    if min(avaible_tanks) > remaining_liters:
        return 0

    for i, tank in enumerate(avaible_tanks):
        if remaining_liters < tank:
            continue

        combinations += min_tanks_filler(avaible_tanks[(i+1):], (remaining_liters-tank), tank_used+1, max_avaible_tanks)

    return combinations

if __name__ == "__main__":
    TANKS = file_read()
    LITERS_TO_FIT = 150

    #first_star(TANKS, LITERS_TO_FIT)
    second_star(TANKS, LITERS_TO_FIT)
