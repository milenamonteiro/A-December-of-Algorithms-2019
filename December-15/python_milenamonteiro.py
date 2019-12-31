import itertools

def cook_dishes(a):
    combinations = []
    dish = str("AB" * a)
    for x in itertools.permutations(dish):
        if x not in combinations:
            combinations.append(x)
    combinations = ["".join(a) for a in combinations]
    return combinations
