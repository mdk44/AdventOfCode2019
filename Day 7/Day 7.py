import re
day5 = __import__("Day 5")
import itertools

input_file = 'Day 7\\Input.csv'
text_file = open(input_file)
lines = [int(i) for i in text_file.read().split(',')]

new_lines = []
for line in lines:
    new_lines.append(line)
day5.process(new_lines)