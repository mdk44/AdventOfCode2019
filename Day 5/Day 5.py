input_file = 'Day 5\\Input.csv'
text_file = open(input_file)
lines = [int(line) for line in text_file.read().split(',')]

x = 0
y = 0
noun = 0
verb = 0
for x in range(0,99):
    for y in range(0,99):
        new_lines = []
        for line in lines:
            new_lines.append(line)
        new_lines[1] = x
        new_lines[2] = y
        start_num = 0
        while new_lines[start_num] != 99:
            input1 = new_lines[start_num + 1]
            input2 = new_lines[start_num + 2]
            output_pos = new_lines[start_num + 3]
            if new_lines[start_num] == 1:
                new_lines[output_pos] = new_lines[input1] + new_lines[input2]
            elif new_lines[start_num] == 2:
                new_lines[output_pos] = new_lines[input1] * new_lines[input2]
            start_num += 4
        if new_lines[0] == 19690720:
            noun = x
            verb = y
            print 'Part 2: ' + str(noun*100 + verb) # Correct!