from random import randint

def not_adjacent(barrel):
    deaths_spin = 0
    deaths_no_spin = 0
    total = 100000
    such_cases = 0

    for _ in range(0, total):
        index = randint(0, bullets - 1)
        x1 = barrel[index]
        if x1 == 0:  #player alive after 1st shot
            such_cases += 1
        #player does not spin
            if index < bullets - 1:
                x2 = barrel[index + 1]
            else:
                x2 = barrel[0]
            if x2 == 1:
                deaths_no_spin += 1
        #player spins
        x2 = barrel[randint(0, bullets - 1)]
        if x2 == 1:
            deaths_spin += 1

    print('If player spins:', end = " ")
    probability_spin = deaths_spin * 100 / total
    print(probability_spin)
    print('If player does not spin:', end = " ")
    probability_no_spin = deaths_no_spin * 100 / such_cases
    print (probability_no_spin)

def adjacent(barrel):
    deaths_spin = 0
    deaths_no_spin = 0
    total = 100000
    such_cases = 0

    for _ in range(0, total):
        index = randint(0, bullets - 1)
        x1 = barrel[index]
        if x1 == 0:  #player alife after 1st shot
            such_cases += 1
        #player does not spin
            if index < bullets - 1:
                x2 = barrel[index + 1]
            else:
                x2 = barrel[0]
            if x2 == 1:
                deaths_no_spin += 1
        #player spins
        x2 = barrel[randint(0, bullets - 1)]
        if x2 == 1:
            deaths_spin += 1

    print('If player spins:', end = " ")
    probability_spin = deaths_spin * 100 / total
    print(probability_spin)
    print('If player does not spin', end = " ")
    probability_no_spin = deaths_no_spin * 100 / such_cases
    print (probability_no_spin)


bullets = int(input('Bullets in barrel: '))
if bullets == 6:
    barrel = [1, 1, 0, 0, 0, 0]
    print("\nADJACENT")
    adjacent(barrel)
    print('\nNOT ADJACENT')
    barrel = [1, 0, 1, 0, 0, 0]
    not_adjacent(barrel)
elif bullets == 5:
    barrel = [1, 1, 0, 0, 0]
    print("\nADJACENT")
    adjacent(barrel)
    print('\nNOT ADJACENT')
    barrel = [1, 0, 1, 0, 0]
    not_adjacent(barrel)

