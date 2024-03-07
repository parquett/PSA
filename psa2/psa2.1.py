import random
import matplotlib.pyplot as plt

nine_wins = []
ten_wins = []
n=10000
nine, ten = 0, 0
aux = [*range(1,n+1,1)]
for _ in range(n):
    a = random.randint(1,7)
    b = random.randint(1,7)
    c = random.randint(1,7)
    if a+b+c == 9:
        nine += 1
    nine_wins.append(nine)
    if a+b+c == 10:
        ten += 1
    ten_wins.append(ten)
print("nine as total",nine,"\nten as total",ten)
plt.plot(aux, nine_wins, label="total 9")
plt.plot(aux, ten_wins, label="total 10")
plt.legend()
plt.show()