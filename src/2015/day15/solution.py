
def file_read():
    ingredients = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(":")

            name = parts[0]

            infos = {}

            for info in parts[1].strip().split(","):
                info_name, score = info.strip().split(" ")
                infos[info_name] = int(score)

            ingredients.append((name, infos))

    return ingredients

def first_star(ingredients, teaspoons):
    for item in ingredients:
        print(item)

    final_score = better_score_tester(ingredients, teaspoons, [], 0, None)

    print(final_score, type(final_score))

def better_score_tester(ingredients: list, total_amount: int, previous_amounts: list, score: int, calorie_total: int|None) -> int:
    remaining_amount = total_amount - sum(previous_amounts)

    if remaining_amount == 0:
        return score_calc(ingredients, previous_amounts, calorie_total)

    if len(ingredients) == len(previous_amounts):
        return score

    amounts = []
    for amount in previous_amounts:
        amounts.append(amount)

    avaible_amount = remaining_amount - len(ingredients) + len(amounts) + 1 #se stesso

    for test_amount in range(avaible_amount, 0, -1):
        amounts.append(test_amount)

        score = max(score, better_score_tester(ingredients, total_amount, amounts, score, calorie_total))

        amounts.pop()

    return score

def score_calc(ingredients: list, spoons: list, calorie_total: int|None):
    final_score = 1
    calories = 0

    scores = {}
    for key, _ in ingredients[0][1].items():
        scores[key] = 0

    for i, (_, infos) in enumerate(ingredients):
        for key, value in infos.items():
            scores[key] = scores[key] + (value * spoons[i])

    for key, value in scores.items():
        if value < 0:
            final_score = 0
            break

        if key == "calories":
            calories += value
            continue

        final_score *= value

    if calorie_total is not None and calories != calorie_total:
        return 0

    return final_score

def second_star(ingredients, teaspoons, calorie_total):
    for item in ingredients:
        print(item)

    final_score = better_score_tester(ingredients, teaspoons, [], 0, calorie_total)

    print(final_score, type(final_score))

if __name__ == "__main__":
    INGREDIENTS = file_read()
    TEASPOONS = 100
    CALORIE_TOTAL = 500

    #first_star(INGREDIENTS, TEASPOONS)
    second_star(INGREDIENTS, TEASPOONS, CALORIE_TOTAL)
