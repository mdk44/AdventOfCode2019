moon1 = [14,4,5,0,0,0]
moon2 = [12,10,8,0,0,0]
moon3 = [1,7,-10,0,0,0]
moon4 = [16,-5,3,0,0,0]

# moon1 = [-1,0,2,0,0,0]
# moon2 = [2,-10,-7,0,0,0]
# moon3 = [4,-8,8,0,0,0]
# moon4 = [3,5,-1,0,0,0]

# print moon1
# print moon2
# print moon3
# print moon4
# print " "

steps = 1000
i = 0

while i in range(0,steps):
    #Check moon 1
    for x in range(0,3):
        pull = 0
        if moon1[x] > moon2[x]:
            pull -= 1
        if moon1[x] < moon2[x]:
            pull += 1
        if moon1[x] > moon3[x]:
            pull -= 1
        if moon1[x] < moon3[x]:
            pull += 1
        if moon1[x] > moon4[x]:
            pull -= 1
        if moon1[x] < moon4[x]:
            pull += 1
        moon1[x+3] += pull
            
    #Check moon 2
    for x in range(0,3):
        pull = 0
        if moon2[x] > moon1[x]:
            pull -= 1
        if moon2[x] < moon1[x]:
            pull += 1
        if moon2[x] > moon3[x]:
            pull -= 1
        if moon2[x] < moon3[x]:
            pull += 1
        if moon2[x] > moon4[x]:
            pull -= 1
        if moon2[x] < moon4[x]:
            pull += 1
        moon2[x+3] += pull

    #Check moon 3
    for x in range(0,3):
        pull = 0
        if moon3[x] > moon1[x]:
            pull -= 1
        if moon3[x] < moon1[x]:
            pull += 1
        if moon3[x] > moon2[x]:
            pull -= 1
        if moon3[x] < moon2[x]:
            pull += 1
        if moon3[x] > moon4[x]:
            pull -= 1
        if moon3[x] < moon4[x]:
            pull += 1
        moon3[x+3] += pull

    #Check moon 4
    for x in range(0,3):
        pull = 0
        if moon4[x] > moon1[x]:
            pull -= 1
        if moon4[x] < moon1[x]:
            pull += 1
        if moon4[x] > moon2[x]:
            pull -= 1
        if moon4[x] < moon2[x]:
            pull += 1
        if moon4[x] > moon3[x]:
            pull -= 1
        if moon4[x] < moon3[x]:
            pull += 1
        moon4[x+3] += pull

    for x in range(0,3):
        moon1[x] += moon1[x+3]
        moon2[x] += moon2[x+3]
        moon3[x] += moon3[x+3]
        moon4[x] += moon4[x+3]

    moon1_energy = (abs(moon1[0]) + abs(moon1[1]) + abs(moon1[2])) * (abs(moon1[3]) + abs(moon1[4]) + abs(moon1[5]))
    moon2_energy = (abs(moon2[0]) + abs(moon2[1]) + abs(moon2[2])) * (abs(moon2[3]) + abs(moon2[4]) + abs(moon2[5]))
    moon3_energy = (abs(moon3[0]) + abs(moon3[1]) + abs(moon3[2])) * (abs(moon3[3]) + abs(moon3[4]) + abs(moon3[5]))
    moon4_energy = (abs(moon4[0]) + abs(moon4[1]) + abs(moon4[2])) * (abs(moon4[3]) + abs(moon4[4]) + abs(moon4[5]))

    i += 1

# print moon1
# print moon2
# print moon3
# print moon4

print("Part 1: " + str(moon1_energy + moon2_energy + moon3_energy + moon4_energy)) # Correct!

# How the eff to do part 2?