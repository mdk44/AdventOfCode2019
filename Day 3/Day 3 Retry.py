import re
import sys
import time
from PIL import Image, ImageDraw

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

grid_rep = {
    CORNER: "+",
    NONE: ".",
    UP: "|",
    ACROSS: "-",
    INTERSECT: "X",
    CENTER: "o",
    CORNER2: "s",
    UP2: "l",
    ACROSS2: "="
}

def image_grid(grid):
    corner = (226, 25, 224)
    none = (0, 0, 0)
    up = (226, 25, 224)
    across = (226, 25, 224)
    intersect = (255, 255, 0)
    center = (175, 175, 175)
    corner2 = (175, 175, 242)
    up2 = (175, 175, 242)
    across2 = (175, 175, 242)
    width = 18000
    height = 12000
    img = Image.new('RGB', (width, height), color = none)
    dr = ImageDraw.Draw(img)
    for y in grid:
        for x in grid[y]:
            if grid[y][x] == CORNER:
                dr.rectangle(((x,y),(x,y)),fill=corner)
            elif grid[y][x] == UP:
                dr.rectangle(((x,y),(x,y)),fill=up)
            elif grid[y][x] == ACROSS:
                dr.rectangle(((x,y),(x,y)),fill=across)
            elif grid[y][x] == INTERSECT:
                dr.rectangle(((x,y),(x,y)),fill=intersect)
            elif grid[y][x] == CENTER:
                dr.rectangle(((x,y),(x,y)),fill=center)
            elif grid[y][x] == CORNER2:
                dr.rectangle(((x,y),(x,y)),fill=corner2)
            elif grid[y][x] == UP2:
                dr.rectangle(((x,y),(x,y)),fill=up2)
            elif grid[y][x] == ACROSS2:
                dr.rectangle(((x,y),(x,y)),fill=across2)
    img.save(output_file)

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            grid_line += grid_rep[grid[y][x]]
        print grid_line

# test1 = ['R8','U5','L5','D3']
# test2 = ['U7','R6','D4','L4']
# test1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# test2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
test1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
test2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

wire1_dir = []
wire1_num = []
wire2_dir = []
wire2_num = []
for i in wire1:
    wire1_dir.append(i[0])
    wire1_num.append(int(i[1:]))
for j in wire2:
    wire2_dir.append(j[0])
    wire2_num.append(int(j[1:]))

grid_size_x = 17020
grid_size_y = 11900
grid_cent_x = 4265
grid_cent_y = 6206

grid = {}
for y in range(0,grid_size_y):
    grid[y] = {}
    for x in range(0,grid_size_x):
        grid[y][x] = NONE
grid[grid_cent_y][grid_cent_x] = CENTER


# Wire 1
cur_x = grid_cent_x
cur_y = grid_cent_y
new_y = 0
new_x = 0
steps = 0
all_steps = 0
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
    steps += 1
    # if cur_x == 3249 and cur_y == 5197:
    #     all_steps += steps


# Wire 2
cur_x = grid_cent_x
cur_y = grid_cent_y
new_y = 0
new_x = 0
ans_x = []
ans_y = []
steps = 0
wire2_steps = []
for i in range(0, len(wire2_dir)):
    if wire2_dir[i] == "U":
        new_y = cur_y - wire2_num[i]
        for y in range(cur_y-1, new_y, -1):
            steps += 1
            if grid[y][cur_x] != NONE:
                grid[y][cur_x] = INTERSECT
                ans_x.append(cur_x)
                ans_y.append(y)
                wire2_steps.append(steps)
            else:
                grid[y][cur_x] = UP2
        grid[new_y][cur_x] = CORNER2
        cur_y = new_y
    if wire2_dir[i] == "D":
        new_y = cur_y + wire2_num[i]
        for y in range(cur_y+1, new_y):
            steps += 1
            if grid[y][cur_x] != NONE:
                grid[y][cur_x] = INTERSECT
                ans_x.append(cur_x)
                ans_y.append(y)
                wire2_steps.append(steps)
            else:
                grid[y][cur_x] = UP2
        grid[new_y][cur_x] = CORNER2
        cur_y = new_y
    if wire2_dir[i] == "R":
        new_x = cur_x + wire2_num[i]
        for x in range(cur_x+1, new_x):
            steps += 1
            if grid[cur_y][x] != NONE:
                grid[cur_y][x] = INTERSECT
                ans_x.append(x)
                ans_y.append(cur_y)
                wire2_steps.append(steps)
            else:
                grid[cur_y][x] = ACROSS2
        grid[cur_y][new_x] = CORNER2
        cur_x = new_x
    if wire2_dir[i] == "L":
        new_x = cur_x - wire2_num[i]
        for x in range(cur_x-1, new_x, -1):
            steps += 1
            if grid[cur_y][x] != NONE:
                grid[cur_y][x] = INTERSECT
                ans_x.append(x)
                ans_y.append(cur_y)
                wire2_steps.append(steps)
            else:
                grid[cur_y][x] = ACROSS2
        grid[cur_y][new_x] = CORNER2
        cur_x = new_x

image_grid(grid)

man_dist = []
for a in range(0, len(ans_x)):
    man_dist.append( abs(ans_x[a] - grid_cent_x) + abs(ans_y[a] - grid_cent_y))
print "Part 1: " + str(min(man_dist))  # Correct but holy crap lol
print "Part 2: "
print wire2_steps