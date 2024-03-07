import random
import matplotlib.pyplot as plt
slots = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
x = int(input("How much you want to bet "))
i = 0
red_wins = []
red_aux = [*range(1, 501, 1)]
number_wins = []
number_aux = [*range(1, 501, 1)]
thousand_bets = 0
red_sum = 0
number_sum = 0
for i in range(500):
    red_slot = random.choice(slots)
    if red_slot % 2 != 0:
        red_sum += x
        red_wins.append(red_sum)
    else:
        red_sum -= x
        red_wins.append(red_sum)

    number_slot = random.choice(slots)
    if number_slot == 18:
        number_sum += 35*x
        number_wins.append(number_sum)
    else:
        number_sum -= x
        number_wins.append(number_sum)
for i in range(1000):
    red_slot = random.choice(slots)
    if red_slot % 2 != 0:
        thousand_bets += 20
    else:
        thousand_bets -= 20

plt.plot(red_aux, red_wins, label="Bets on red")
plt.plot(number_aux, number_wins, label="Bets on 18")
plt.xlabel('')
plt.ylabel('')
plt.legend()
print(red_wins)
print("If you would make 1000 bets of 20$ on red you would have" , thousand_bets)
print("If you would make 500 bets on red you would have" , red_sum)
print("If you would make 500 bets on number 18 you would have" , number_sum)
plt.show()