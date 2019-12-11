input_file = 'Day 10\\Test1.csv'
# input_file = 'Day 10\\Test2.csv'
# input_file = 'Day 10\\Test3.csv'
# input_file = 'Day 10\\Test4.csv'
# input_file = 'Day 10\\Test5.csv'
# input_file = 'Day 10\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            grid_line += grid[y][x]
        print grid_line

grid = {}
for y in range(0,len(lines)):
    grid[y] = {}
    for x in range(0,len(lines[0])):
        grid[y][x] = lines[y][x]

print_grid(grid)