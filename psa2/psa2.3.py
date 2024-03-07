import random

import numpy as np
counter = 0
n = 10000
for _ in range(n):
    a = random.randint(1,100)
    b = 100-a
    mx, mn = max(a,b), min(a,b)
    c = random.randint(1,mx)
    if max(mx-c, mn, c) < 50:
        counter += 1
print(counter / n)



# def istriangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
# for _ in range(n):
#     x = random.uniform(0, 1.0)
#     y = random.uniform(x, 1.0)
#     if istriangle(x, y - x, 1 - y)==True:
#         counter+=1
# print(counter / n)