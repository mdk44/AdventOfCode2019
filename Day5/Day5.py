input_file = 'Day5\\Input.csv'
text_file = open(input_file)
lines = [int(line) for line in text_file.read().split(',')]
# lines = [3,0,4,0,99]

class ValueAndParamPair:
    def __init__(self, index, parameter):
        self.index = index
        self.parameter = parameter
    def get_value(self, puzzle_input):
        if self.parameter == 0:
            return puzzle_input[self.index]
        return self.index

def get_parameter_pairs(int_code, int_code_slice):
    params = int_code[0:len(int_code) - 2]
    params = params[len(params)::-1]
    pairs = []
    for i in range(len(params)):
        pairs.append(ValueAndParamPair(int_code_slice[i+1], int(params[i])))
    return pairs

def opcode_1(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    puzzle_input[puzzle_input[index + 3]] = value1 + value2
    return index + 4

def opcode_2(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    puzzle_input[puzzle_input[index + 3]] = value1 * value2
    return index + 4

def opcode_3(puzzle_input, index):
    user_input = init_input
    puzzle_input[puzzle_input[index + 1]] = int(user_input)
    return index + 2

def opcode_4(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(3, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    print("Output: " + str(param_pairs[0].get_value(puzzle_input)))
    return index + 2

def opcode_5(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(4, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    value = param_pairs[0].get_value(puzzle_input)
    if value != 0:
        return param_pairs[1].get_value(puzzle_input)
    return index + 3

def opcode_6(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(4, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    if param_pairs[0].get_value(puzzle_input) == 0:
        return param_pairs[1].get_value(puzzle_input)
    return index + 3

def opcode_7(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    if value1 < value2:
        puzzle_input[puzzle_input[index + 3]] = 1
    else:
        puzzle_input[puzzle_input[index + 3]] = 0
    return index + 4

def opcode_8(puzzle_input, index):
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    if value1 == value2:
        puzzle_input[puzzle_input[index + 3]] = 1
    else:
        puzzle_input[puzzle_input[index + 3]] = 0
    return index + 4

opcodes = {
    1: opcode_1,
    2: opcode_2,
    3: opcode_3,
    4: opcode_4,
    5: opcode_5,
    6: opcode_6,
    7: opcode_7,
    8: opcode_8,
}

def process(puzzle_input):
    index = 0
    while True:
        int_code = puzzle_input[index]
        if int_code == 99:
            break
        if int_code in opcodes:
            handler = opcodes[int_code]
        else:
            final_int = int(str(int_code)[-2:])
            if final_int in opcodes:
                handler = opcodes[final_int]
            else:
                print("Unable to find handler for int_code: " + str(int_code) + " at index: " + str(index))
                break
        index = handler(puzzle_input, index)

# Part 1
init_input = 1
new_lines = []
for line in lines:
    new_lines.append(line)
start_num = 0

if __name__ == '__main__':
    process(new_lines) # Correct!

# Part 2
init_input = 5
new_lines = []
for line in lines:
    new_lines.append(line)
start_num = 0

if __name__ == '__main__':
    process(new_lines) # Correct! Thanks Ben