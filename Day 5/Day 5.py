# input_file = 'Day 5\\Input.csv'
# text_file = open(input_file)
# lines = [int(line) for line in text_file.read().split(',')]

lines = [3,0,4,0,99]

init_input = 1
new_lines = []
for line in lines:
    new_lines.append(line)
start_num = 0

input1 = new_lines[start_num]
# will revisit





while new_lines[start_num] != 99:
    if new_lines[start_num] == 1:
        input1 = new_lines[start_num + 1]
        input2 = new_lines[start_num + 2]
        output_pos = new_lines[start_num + 3]
        new_lines[output_pos] = new_lines[input1] + new_lines[input2]
        start_num += 4
    elif new_lines[start_num] == 2:
        input1 = new_lines[start_num + 1]
        input2 = new_lines[start_num + 2]
        output_pos = new_lines[start_num + 3]
        new_lines[output_pos] = new_lines[input1] * new_lines[input2]
        start_num += 4
    elif new_lines[start_num] == 3:
        input1 = init_input
        output_pos = new_lines[start_num + 1]
        new_lines[output_pos] = input1
        start_num += 2
    elif new_lines[start_num] == 4:
        output_pos = new_lines[start_num + 1]
        print new_lines[output_pos]
        start_num += 2
print new_lines

test1 = 1002
test2 = str(test1)
testlen = len(test2)
print int(test2[-2:])
print test2[-testlen]
print testlen