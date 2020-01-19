import random

counter = 0
algList = []
commands = []
command = ""
rand = random.randrange(0, 1029362)

with open("/Users/joochanshin/Desktop/htm.txt") as f:
    for line in f:
        counter += 1
        algList.append(line)

for i in range(0, len(algList[rand])):
    if i%2 == 1:
        command = command + algList[rand][i]
        commands.append(command)
        command = ""
    else:
        command = command + algList[rand][i]

print(commands)

