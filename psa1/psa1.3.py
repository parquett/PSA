import random
AnaWins = 0
for _ in range(0,1000):
    AnaPoints = 0
    DanPoints = 0
    servesFirst = random.randint(0, 1)
    while(AnaPoints != 25 and DanPoints != 25):
        if(servesFirst == 0):
            k = random.randint(0, 100)
            if(k <= 70):
                AnaPoints += 1
            else:
                servesFirst = 1
        if(servesFirst == 1):
            k = random.randint(0, 100)
            if (k <= 50):
                DanPoints += 1
            else:
                servesFirst = 0
    if(AnaPoints==25):
        AnaWins+=1
print("Probability, that Ana will win -", AnaWins/1000)
