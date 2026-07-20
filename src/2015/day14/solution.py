
def file_read():
    reindeers = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line=line.replace("can fly","").replace("seconds, but then must rest for","").replace("seconds.","")

            parts = cleaned_line.split("  ")

            km_s, seconds = parts[1].split(" km/s for ")

            reindeers.append((parts[0], (int(km_s), int(seconds)), int(parts[2])))

    return reindeers

def first_star(reindeers, timer):
    longest_distance = 0

    for _, (distance_per_second, for_how_long), rest in reindeers:
        remaining_timer = timer
        deer_distance = 0

        needs_rest = False
        while remaining_timer > 0:

            if needs_rest:
                remaining_timer -= rest
                needs_rest = False
                continue

            if for_how_long > remaining_timer:
                deer_distance += distance_per_second * remaining_timer
            else:
                deer_distance += distance_per_second * for_how_long

            remaining_timer -= for_how_long

            needs_rest = True

        longest_distance = max(longest_distance, deer_distance)

    print("longest distance", longest_distance)

def second_star(reindeers, timer):
    reindeers_list = []

    scores = []

    distances_traveled = []
    heads_i = []

    for i, (name, (distance, time), rest) in enumerate(reindeers):
        reindeers_list.append([(name, distance, time, rest), False, time])
        distances_traveled.append(0)
        scores.append(0)

    for _ in range(timer):

        for i,[(name,distance_per_second,stamina_time,rest_time), is_resting, time_needed] in enumerate(reindeers_list):
            time_needed -= 1

            if not is_resting:
                distances_traveled[i] = distances_traveled[i] + distance_per_second

            if time_needed == 0:
                is_resting = not is_resting

                if is_resting:
                    time_needed = rest_time
                else:
                    time_needed = stamina_time

            reindeers_list[i] = [(name, distance_per_second, stamina_time, rest_time), is_resting, time_needed]

        longest_distance = max(distances_traveled)

        for i, distance in enumerate(distances_traveled):
            if distance != longest_distance:
                if i in heads_i:
                    heads_i.remove(i)
                continue

            if i not in heads_i:
                heads_i.append(i)

            scores[i] = scores[i] + 1

    print(sum(scores), scores, " the highest is ", max(scores))

if __name__ == "__main__":
    REINDEERS = file_read()
    TIMER = 2503

    #first_star(REINDEERS, TIMER)
    second_star(REINDEERS, TIMER)
