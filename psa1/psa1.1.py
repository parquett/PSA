import random
#0-tail
#1-head
games = 100000
money = 0
for _ in range(games):
    win = 0
    j = 1
    c = random.randint(0, 1)
    while c == 0:
        c = random.randint(0, 1)
        win = 2**j
        j += 1
    money += win
print(money/games)