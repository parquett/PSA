#0-tail
#1-head
import random
import matplotlib.pyplot as plt

n=1000
heads = []
games = [*range(1,n+1,1)]
counter = 0
for _ in range(n):
    x = random.randint(0, 1)
    if x==1: counter+=1
    if counter>=35 and counter<=65: heads.append(counter)
    else: heads.append(0)
print(counter)

# plt.ylim([35,66])
# plt.xlim([1,1000])
plt.plot(games, heads)
plt.show()
