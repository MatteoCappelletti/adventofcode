
def file_read():
    areas = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            areas.append(str(line.strip()))

    return areas

def first_star(areas):
    total_surface = 0

    for area in areas:
        measures = area.split("x")
        l = int(measures[0])
        w = int(measures[1])
        h = int(measures[2])

        surface = 2*l*w + 2*w*h + 2*h*l

        surface += min(l*w, w*h, h*l)

        total_surface += surface

    print(f"total surface = [{total_surface}]")

def second_star(areas):
    total = 0


    for area in areas:
        cose = []

        measures = area.split("x")
        l = int(measures[0])
        w = int(measures[1])
        h = int(measures[2])

        cose.append(l)
        cose.append(w)
        cose.append(h)

        s1, s2 = sorted(cose)[:2]

        ribbon = 2*(int(s1)) + 2*(int(s2))
        bow = l*w*h

        total += ribbon + bow

        print(area, ribbon, bow)

    print(total)

if __name__ == "__main__":
    AREAS = file_read()

    #first_star(AREAS)
    second_star(AREAS)
