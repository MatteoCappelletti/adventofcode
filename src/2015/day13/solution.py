
def file_read():
    combinations = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = line.replace("would", "").replace("happiness units by sitting next to", "").replace(".", "")

            infos = cleaned_line.split()

            subject = infos[0]
            happiness = (int(infos[2]) * - 1) if infos[1] == "lose" else int(infos[2])
            sitted_next = infos[3]

            combinations.append((subject, happiness, sitted_next))

    subject_names = []
    for subject, _, _ in combinations:
        if subject not in subject_names:
            subject_names.append(subject)

    subject_interactions = []
    for subject in subject_names:
        subject_interactions.append((subject, []))

    for subject, happiness, sitted_next in combinations:
        for si_subject, interactions in subject_interactions:
            if subject == si_subject:
                interactions.append((sitted_next, happiness))

    return subject_interactions

def first_star(interactions: list):
    #print(interactions)

    print("totale happiness", table_happiness_tester(interactions, [], 0))

def table_happiness_tester(interactions: list, previous_table: list, happiness: int):
    if len(previous_table) == len(interactions):
        return table_happiness_counter(interactions, previous_table)

    table = copy_list(previous_table)

    for subject, relationships in interactions:
        if len(table) == 0:
            table.append(subject)

        if subject != table[-1]:
            continue

        for sitted_next, _ in relationships:
            if sitted_next in table:
                continue

            table.append(sitted_next)

            happiness = max(happiness, table_happiness_tester(interactions, table, happiness))

            table.pop()

    return happiness

def copy_list(list_to_copy: list):
    new_list = []

    for item in list_to_copy:
        new_list.append(item)

    return new_list

def table_happiness_counter(interactions, table):
    total_happiness = 0

    for sit_i, person in enumerate(table):
        for subject, relationships in interactions:
            if person != subject:
                continue

            for sitted_next, happiness in relationships:
                sitted_left = table[sit_i - 1]
                try:
                    sitted_right = table[sit_i + 1]
                except IndexError:
                    sitted_right = table[0]

                if sitted_next not in [sitted_left, sitted_right]:
                    continue

                total_happiness += happiness

    return total_happiness

def second_star(interactions: list, me: str):
    mine_interactions = []

    for person, relationship in interactions:
        relationship.append((me, 0))
        mine_interactions.append((person, 0))

    interactions.append((me, mine_interactions))

    print(interactions)

    print("totale happiness", table_happiness_tester(interactions, [], 0))

if __name__ == "__main__":
    INTERACTIONS = file_read()
    ME = "Matteo"

    #first_star(INTERACTIONS)
    second_star(INTERACTIONS, ME)
