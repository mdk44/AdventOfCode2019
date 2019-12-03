# Test Data
# input_text = '1,0,0,0,99'
# input_text = '2,3,0,3,99'
# input_text = '2,4,4,5,99,0'
# input_text = '1,1,1,4,99,5,6,0,99'
# lines = [int(line) for line in input_text.split(',')]
#    THESE ARE ALL CORRECT

input_file = 'Day 2\\Input.csv'
text_file = open(input_file)
lines = [int(line) for line in text_file.read().split(',')]

new_lines = []
for line in lines:
    new_lines.append(line)

new_lines[1] = 12
new_lines[2] = 2
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

print "Part 1: " + str(new_lines[0])  #Correct!

#rerun part 1 with different values for new_lines 1 and new_lines 2 and run until my 'output' position

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
                new_lines[output_pos] = lines[input1] + lines[input2]
            elif new_lines[start_num] == 2:
                new_lines[output_pos] = lines[input1] * lines[input2]
            start_num += 4
        if new_lines[0] == 19690720:
            noun = x
            verb = y
            print 'Part 2: ' + str(noun*100 + verb)