input_file = 'Day 6\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

test_inp = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

for i in range(0,len(test_inp)):
    place = test_inp[i].find(')')
    obj = test_inp[i][0:place]
    orb = test_inp[i][place + 1:]