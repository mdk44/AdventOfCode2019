import re
import sys
import itertools
sys.path.insert(0, 'Day5')
from Day5 import opcodes, get_parameter_pairs
from itertools import permutations

input_file = 'Day7\\Input.csv'
text_file = open(input_file)
lines = [int(i) for i in text_file.read().split(',')]

new_lines = []
for line in lines:
    new_lines.append(line)