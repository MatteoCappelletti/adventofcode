
import json as JSON

def file_read():
    json_nodes = ""

    with open("./input.txt", 'r', encoding='utf-8') as file:
        json_nodes = JSON.load(file)

    return json_nodes

def first_star(json):
    print("totale", json_explorer(json))

def json_explorer(json_from_node):
    total = 0

    for item in json_from_node:
        #print(item, type(item))

        if isinstance(item, int):
            total += item

        elif isinstance(item, list):
            total += json_explorer(item)

        elif isinstance(item, dict):
            total += json_explorer(item)

        elif isinstance(item, str):
            try:
                value = json_from_node[item]

                if isinstance(value, int):
                    total += value
                else:
                    total += json_explorer(json_from_node[item])

            except TypeError:
                #do nothing
                pass

        else:
            print("non trovato tipo", item, type(item))

    return total


def second_star(json, exception):
    print("totale", second_star_json_explorer(json, exception))

def second_star_json_explorer(json_from_node, exception: str):
    total = 0

    for item in json_from_node:
        if isinstance(json_from_node, dict) and exception in json_from_node.values():
            continue

        if isinstance(item, int):
            total += item

        elif isinstance(item, list):
            total += second_star_json_explorer(item, exception)

        elif isinstance(item, dict):
            if exception not in item.values():
                total += second_star_json_explorer(item, exception)

        elif isinstance(item, str):
            try:
                value = json_from_node[item]

                if isinstance(value, int):
                    total += value
                else:
                    total += second_star_json_explorer(json_from_node[item], exception)

            except TypeError:
                #do nothing
                pass

        else:
            print("non trovato tipo", item, type(item))

    return total

if __name__ == "__main__":
    JSON_FILE = file_read()
    EXCEPT = "red"

    #first_star(JSON_FILE)
    second_star(JSON_FILE, EXCEPT)
