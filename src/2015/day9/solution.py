
def file_read():
    travel_distances = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split("=")

            distance_value = int(parts[1].strip())

            cities = parts[0].split(" to ")

            city1 = cities[0].strip()
            city2 = cities[1].strip()

            travel_distances.append(((city1, city2), distance_value))

    nodes_names = []
    for (city1, city2), _ in travel_distances:
        if city1 not in nodes_names:
            nodes_names.append(city1)
        if city2 not in nodes_names:
            nodes_names.append(city2)

    nodes = []
    for city_name in nodes_names:
        distances = {}

        for cities, value in travel_distances:
            if city_name not in cities:
                continue

            next_city = cities[0] if cities[0] != city_name else cities[1]

            distances[next_city] = value

        nodes.append((city_name, distances))

    return nodes

def first_star(nodes):
    distance = min_path_calc(nodes, [], 1_000_000)
    print("distance", distance)

def min_path_calc(nodes: list, previous_path: list, shorter_distance: int):
    path = []
    for city in previous_path:
        path.append(city)

    for city, destinations in nodes:
        if city in path:
            continue

        path.append(city)

        if len(path) == len(nodes):
            try_distance = complessive_distance_value(nodes, path)
            return min(shorter_distance, try_distance)

        if len(path) > 1 and path[len(path) - 2] not in destinations.keys():
            return None

        new_distance = min_path_calc(nodes, path, shorter_distance)

        if new_distance is not None:
            shorter_distance = new_distance

        path.pop()

    return shorter_distance

def complessive_distance_value(nodes: list, path: list):
    distance_value = 0

    for i in range(0, (len(path) - 1), 1):
        actual_city = path[i]
        next_city = path[i + 1]

        for city, destinations in nodes:
            if actual_city == city and next_city in destinations.keys():
                distance_value += destinations[next_city]
                break

    print("DIST", path, distance_value)
    return distance_value

def second_star(nodes):
    distance = max_path_calc(nodes, [], 0)
    print("distance", distance)

def max_path_calc(nodes: list, previous_path: list, longest_distance: int):
    path = []
    for city in previous_path:
        path.append(city)

    for city, destinations in nodes:
        if city in path:
            continue

        path.append(city)

        if len(path) == len(nodes):
            try_distance = complessive_distance_value(nodes, path)
            return max(longest_distance, try_distance)

        if len(path) > 1 and path[len(path) - 2] not in destinations.keys():
            return None

        new_distance = max_path_calc(nodes, path, longest_distance)

        if new_distance is not None:
            longest_distance = new_distance

        path.pop()

    return longest_distance

if __name__ == "__main__":
    NODES = file_read()

    #first_star(NODES)
    second_star(NODES)
