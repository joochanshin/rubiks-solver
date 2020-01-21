import random

counter = 0
algList = []
commands = []
command = ""
rand = random.randrange(0, 1029362)

with open("/Users/joochanshin/Desktop/htm.txt") as f:
    for line in f:
        counter += 1
        if line[0] + line[1] == 'R1':
            for i in range(0,len(line)):
                if i%2 == 1:
                    command = command + line[i]
                    commands.append(command)
                    command = ""
                else:
                    command = command + line[i]
            algList.append(commands)
            commands = []
            command = ""

# for i in range(0, len(algList[rand])):
#     if i%2 == 1:
#         command = command + algList[rand][i]
#         commands.append(command)
#         command = ""
#     else:
#         command = command + algList[rand][i]
rand2 = random.randrange(0, len(algList))
print(algList[rand2], rand2, len(algList))

