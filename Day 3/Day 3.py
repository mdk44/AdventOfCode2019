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

wire1_dir = []
wire1_num = []
wire2_dir = []
wire2_num = []
for i in test1:
    wire1_dir.append(i[0])
    wire1_num.append(int(i[1:]))
for j in test2:
    wire2_dir.append(j[0])
    wire2_num.append(int(j[1:]))

grid = {}
for y in range(0,100):
    grid[y] = {}
    for x in range(0,100):
        grid[y][x] = NONE
grid[50][50] = CENTER


# Wire 1
cur_x = 50
cur_y = 50
new_y = 0
new_x = 0
for i in range(0, len(wire1_dir)):
    if wire1_dir[i] == "U":
        new_y = cur_y - wire1_num[i]
        for y in range(cur_y-1, new_y, -1):
            grid[y][cur_x] = UP
        grid[new_y][cur_x] = CORNER
        cur_y = new_y
    if wire1_dir[i] == "D":
        new_y = cur_y + wire1_num[i]
        for y in range(cur_y+1, new_y):
            grid[y][cur_x] = UP
        grid[new_y][cur_x] = CORNER
        cur_y = new_y
    if wire1_dir[i] == "R":
        new_x = cur_x + wire1_num[i]
        for x in range(cur_x+1, new_x):
            grid[cur_y][x] = ACROSS
        grid[cur_y][new_x] = CORNER
        cur_x = new_x
    if wire1_dir[i] == "L":
        new_x = cur_x - wire1_num[i]
        for x in range(cur_x-1, new_x, -1):
            grid[cur_y][x] = ACROSS
        grid[cur_y][new_x] = CORNER
        cur_x = new_x

# Wire 2
cur_x = 50
cur_y = 50
new_y = 0
new_x = 0
for i in range(0, len(wire2_dir)):
    if wire2_dir[i] == "U":
        new_y = cur_y - wire2_num[i]
        for y in range(cur_y-1, new_y, -1):
            if grid[y][cur_x] != NONE:
                grid[y][cur_x] = INTERSECT
            else:
                grid[y][cur_x] = UP
        grid[new_y][cur_x] = CORNER
        cur_y = new_y
    if wire2_dir[i] == "D":
        new_y = cur_y + wire2_num[i]
        for y in range(cur_y+1, new_y):
            if grid[y][cur_x] != NONE:
                grid[y][cur_x] = INTERSECT
            else:
                grid[y][cur_x] = UP
        grid[new_y][cur_x] = CORNER
        cur_y = new_y
    if wire2_dir[i] == "R":
        new_x = cur_x + wire2_num[i]
        for x in range(cur_x+1, new_x):
            if grid[cur_y][x] != NONE:
                grid[cur_y][x] = INTERSECT
            else:
                grid[cur_y][x] = ACROSS
        grid[cur_y][new_x] = CORNER
        cur_x = new_x
    if wire2_dir[i] == "L":
        new_x = cur_x - wire2_num[i]
        for x in range(cur_x-1, new_x, -1):
            if grid[cur_y][x] != NONE:
                grid[cur_y][x] = INTERSECT
            else:
                grid[cur_y][x] = ACROSS
        grid[cur_y][new_x] = CORNER
        cur_x = new_x

print_grid(grid)