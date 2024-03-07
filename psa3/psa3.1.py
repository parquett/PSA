# # by formula
# captured1 = 50
# captured2 = 200
# tagged2 = 8
# N = captured1 * captured2 / tagged2
# print("The estimated number of deer in the Codrii reserve is:", N)


# by sim
import random

n = 1000
tagged_ = 50
captured_ = 200

for deer_number in range(250, 2000, 50):
    tagged_count = 0
    for _ in range(n):
        deer = [1 if i < tagged_ else 0 for i in range(deer_number)]
        random.shuffle(deer)
        captured = deer[:captured_]
        tagged_count += captured.count(1)

    print(f"{tagged_count/n} / {deer_number} estimated deers")