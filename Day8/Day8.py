import re
import sys
import time
from PIL import Image, ImageDraw # Does not seem to work in Python 3.8

input_file = 'Day8\\Input.csv'
output_file = 'Day8\\Password.png'
text_file = open(input_file)
lines = [int(line) for line in text_file.read()]

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            if grid[y][x] == 0:
                grid_line += "  "
            elif grid[y][x] == 1:
                grid_line += " O"
        print(grid_line)

def image_grid(grid):
    no_fill = (255, 255, 255)
    zero = (0, 0, 0)
    one = (226, 25, 224)
    width = 625
    height = 150
    img = Image.new('RGB', (width, height), color = no_fill)
    dr = ImageDraw.Draw(img)
    for y in grid:
        for x in grid[y]:
            if grid[y][x] == 0:
                dr.rectangle(((25*x,25*y),(25*x+25,25*y+25)),fill=zero,width=5)
            elif grid[y][x] == 1:
                dr.rectangle(((25*x,25*y),(25*x+25,25*y+25)),fill=one,width=5)
    img.save(output_file)

grid = {}
for y in range(0,6):
    grid[y] = {}
    for x in range(0,25):
        grid[y][x] = 2

start_num = 0
num_0 = 20000
num_1 = 0
num_2 = 0

while start_num < len(lines):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    x = 0
    y = 0
    for i in range(start_num, start_num + 150):
        if lines[i] == 0:
            count_0 += 1
            if grid[y][x] == 2:
                grid[y][x] = 0
        elif lines[i] == 1:
            count_1 += 1
            if grid[y][x] == 2:
                grid[y][x] = 1
        elif lines[i] == 2:
            count_2 += 1
        x += 1
        if x == 25:
            x = 0
            y += 1
    if count_0 < num_0:
        num_0 = count_0
        num_1 = count_1
        num_2 = count_2
    start_num += 150

print("Part 1 -  0: " + str(num_0) + "  1x2: " + str(num_1 * num_2))  # Correct!
print("")
print("Part 2:")
print_grid(grid)
image_grid(grid)