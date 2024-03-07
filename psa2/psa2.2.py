import numpy as np
counter = 0
n = 10000
for _ in range(n):
    values = np.random.uniform(low=0, high=1, size=2)
    a = min(values)
    b = abs(values[0] - values[1])
    print(values)
    if a < 0.5 and b < 0.5 and 0.5 < a + b:
        counter += 1
print(counter / n)
