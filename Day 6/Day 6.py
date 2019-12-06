input_file = 'Day 6\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

test_inp = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

#basically I want to look at, for every new thing on the right side, if there is an existing left side so that I can add an orbit + 1