import random

n = 100000
money=0
for _ in range(0,n):
    x = random.uniform(0, 1)
    # print("x",x)
    for i in range(1,n):
        y = random.uniform(0, 1)
        # print("y",y)
        if y > x:
            win = i - 1
            money+=win
            break
print(money/n)