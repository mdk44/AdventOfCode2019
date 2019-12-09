input_file1 = 'Day 3\\Wire1.csv'
text_file1 = open(input_file1)
input_file2 = 'Day 3\\Wire2.csv'
text_file2 = open(input_file2)
wire1 = text_file1.read().split(',')
wire2 = text_file2.read().split(',')
output_file = 'Day 3\\Wires.png'

CORNER = 0
NONE = 1
UP = 2
ACROSS = 3
INTERSECT = 4
CENTER = 5
CORNER2 = 6
UP2 = 7
ACROSS2 = 8


