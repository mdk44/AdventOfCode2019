import re
import Day5
import itertools

input_file = 'Day7\\Input.csv'
text_file = open(input_file)
lines = [int(i) for i in text_file.read().split(',')]

new_lines = []
for line in lines:
    new_lines.append(line)