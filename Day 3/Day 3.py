import re
import sys
import time
from PIL import Image, ImageDraw

CORNER = 0
NONE = 1
UP = 2
ACROSS = 3
INTERSECT = 4
CENTER = 5

grid_rep = {
    CORNER: "+",
    NONE: ".",
    UP: "|",
    ACROSS: "-",
    INTERSECT: "X",
    CENTER: "o"
}

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            grid_line += grid_rep[grid[y][x]]
        print grid_line

input_file1 = 'Day 3\\Wire1.csv'
text_file1 = open(input_file1)
input_file2 = 'Day 3\\Wire2.csv'
text_file2 = open(input_file2)
wire1 = text_file1.read().split(',')
wire2 = text_file2.read().split(',')

test1 = ['R8','U5','L5','D3']
test2 = ['U7','R6','D4','L4']

# test1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# test2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# test1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# test2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

start_x = 50
start_y = 50
grid = {}
for y in range(0,100):
    grid[y] = {}
    for x in range(0,100):
        grid[y][x] = NONE
grid[50][50] = CENTER

print_grid(grid)