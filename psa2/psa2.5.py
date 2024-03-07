import random
import math

def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    root1, root2 = 0, 0
    # checking condition for discriminant
    if dis > 0:
        root1 = ((-b + sqrt_val) / (2 * a))
        root2 = ((-b - sqrt_val) / (2 * a))
    return root1, root2


n = 10000
posCounter, realCounter = 0, 0
for _ in range(n):
    b = random.uniform(-1, 2)
    c = random.uniform(-1, 2)
    r1,r2=equationroots(1,b,c)
    if(r1>0 and r2>0): posCounter+=1
    if(r1==0 and r2==0): realCounter+=1
print("both roots are real",realCounter/n)
print("both roots are positive",posCounter/n)