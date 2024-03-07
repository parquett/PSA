import random

diameter = 1
square_edge = diameter * 2
coins = 10000
coins_in_square = 0

for i in range(coins):
    x = random.uniform(0, square_edge)
    y = random.uniform(0, square_edge)
    if diameter <= x < square_edge and diameter <= y < square_edge:
        coins_in_square += 1

print("Number of coins in square:", coins_in_square)
