from numpy import random
from math import sqrt

#x = random.uniform(low=-1.0, high=1.0, size=None)

such_cases = 0

good_cases1 = 0
good_cases2 = 0
good_cases3 = 0
good_cases4 = 0

for i in range(0, 10000):
    x = random.uniform(low=-1.0, high=1.0, size=None)
    y = random.uniform(low=0.0, high=1.0, size=None)
    if x**2 + y** 2 <= 1:
        such_cases += 1
        if x > 0:
            good_cases1 += 1
        if (sqrt(x**2 + y**2)) < 0.5:
            good_cases2 += 1
        if (sqrt(x**2 + y**2)) > 0.5:
            good_cases3 += 1
        if sqrt(x**2 + (y-0.5)**2) <= 0.5:
            good_cases4 += 1
            
print(f'It lands in the right half of the target: {good_cases1/such_cases}')
print(f'Its distance from the center is less than 5 inches: {good_cases2/such_cases}')
print(f'Its distance from the center is greater than 5 inches: {good_cases3/such_cases}')
print(f'It lands within 5 inches of the point (0, 5): {good_cases4/such_cases}')