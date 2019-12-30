input_file = 'Day 6\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
# lines = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'] # Part 1
# lines = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'] # Part 2

inp = dict()
inp2 = dict()

for i in range(0,len(lines)):
    place = lines[i].find(')')
    obj = lines[i][0:place]
    orb = lines[i][place + 1:]
    if obj not in inp:
        inp[obj] = []
    inp[obj].append(orb)
    inp2[orb] = obj

# print(inp)
# print(inp2)
places_ive_been = dict()

def count_orbits(obj, depth):
    count_orb = len(inp[obj])*depth
    for o in inp[obj]:
        if o in inp:
            count_orb += count_orbits(o, depth + 1)
    return count_orb

def count_hops(start, end, hops):
    places_i_can_go = []
    places_ive_been[start] = True
    if start in inp2:
        places_i_can_go.append(inp2[start])
    if start in inp:
        for place in inp[start]:
            places_i_can_go.append(place)
    for place in places_i_can_go:
        if place == end:
            return hops
        if place in places_ive_been:
            continue
        result = count_hops(place, end, hops + 1)
        if result is not None:
            return result

print(count_orbits('COM',1)) # Correct!
print(count_hops('YOU', 'SAN', -1)) # Correct!  The -1 is removing the hop from YOU to first planet