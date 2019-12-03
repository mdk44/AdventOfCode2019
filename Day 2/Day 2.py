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

new_lines = lines
new_lines[1] = 12
new_lines[2] = 2
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

print "Part 1: " + str(new_lines[0])  #Correct!

start_num = 0
output_num = 0
while new_lines[start_num] != 99:
    new_lines = lines
    new_lines[1] = 12
    new_lines[2] = 2
    input1 = new_lines[start_num + 1]
    input2 = new_lines[start_num + 2]
    if new_lines[start_num] == 1:
        output_num = lines[input1] + lines[input2]
    elif new_lines[start_num] == 2:
        output_num = lines[input1] * lines[input2]
    start_num += 4
    print output_num
    if output_num == 19690720:
        noun = lines[input1]
        verb = lines[input2]
        print noun
        print verb
    ##crap
