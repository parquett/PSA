import random

caught = 0
cost = 0
for _ in range(730):
    k = random.randint(0, 100)
    hairy = random.randint(0, 100)
    if hairy <= 2:
        cost += 6
    else:
        if k <= 5:
            if caught < 1:
                cost += 50
                caught += 1
            elif caught < 2:
                cost += 150
                caught += 1
            else: cost += 300
print("expected payment of Jora",cost)
print("payment by law-abiding students",6*730)