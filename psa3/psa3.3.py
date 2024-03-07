from random import randint
#if the seat assigned to the 16th person to board is free when the last person boards,
#then it was also free when the 16th person boarded, so she would have taken it then, a contradiction
good_cases = 0

for j in range(0, 10000):
    people = []
    seats = []
    for i in range(1, 101):
        people.append(i)
        seats.append(i)
    seat = randint(2, 100)
    seats.remove(seat)
    for i in range(2, 100):
        if i in seats:
            seats.remove(i)
        else:
            index = randint(0, len(seats)-1)
            seats.remove(seats[index])
        if seats[0] == 100:
            good_cases += 1

print(good_cases/10000)