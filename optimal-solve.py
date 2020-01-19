import random

counter = 0
algList = []
rand = random.randrange(0, 1029362)

with open("/Users/joochanshin/Desktop/htm.txt") as f:
    for line in f:
        counter += 1
        algList.append(line)

print(algList[rand], rand)