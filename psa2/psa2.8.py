import random

n = 10
simulations = 10000
counter = 0

for _ in range(simulations):
    # randomly assign seats for lunch
    lunch_seating = list(range(n))
    random.shuffle(lunch_seating)

    # randomly assign seats for dinner
    dinner_seating = list(range(n))
    random.shuffle(dinner_seating)

    # check if no two people sit next to each other at both meals
    success = True
    for i in range(n):
        if lunch_seating[i] == dinner_seating[(i + 1) % n] or lunch_seating[i] == dinner_seating[(i - 1) % n]:
            success = False
            break

    if success:
        counter += 1

print(counter / simulations)

