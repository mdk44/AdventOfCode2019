input_file1 = 'Day 3\\Wire1.csv'
text_file1 = open(input_file1)
input_file2 = 'Day 3\\Wire2.csv'
text_file2 = open(input_file2)
wire1 = text_file1.read().split(',')
wire2 = text_file2.read().split(',')

CORNER = 0
NONE = 1
UP = 2
ACROSS = 3
INTERSECT = 4
CENTER = 5
CORNER2 = 6
UP2 = 7
ACROSS2 = 8

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

grid = dict()

# Wire 1
cur_x = 0
cur_y = 0
new_y = 0
new_x = 0
for i in range(0, len(wire1_dir)):
    if wire1_dir[i] == "U":
        new_y = cur_y - wire1_num[i]
        for y in range(cur_y-1, new_y, -1):
            grid[y, cur_x] = UP
        grid[new_y, cur_x] = CORNER
        cur_y = new_y
    if wire1_dir[i] == "D":
        new_y = cur_y + wire1_num[i]
        for y in range(cur_y+1, new_y):
            grid[y, cur_x] = UP
        grid[new_y, cur_x] = CORNER
        cur_y = new_y
    if wire1_dir[i] == "R":
        new_x = cur_x + wire1_num[i]
        for x in range(cur_x+1, new_x):
            grid[cur_y, x] = ACROSS
        grid[cur_y, new_x] = CORNER
        cur_x = new_x
    if wire1_dir[i] == "L":
        new_x = cur_x - wire1_num[i]
        for x in range(cur_x-1, new_x, -1):
            grid[cur_y, x] = ACROSS
        grid[cur_y, new_x] = CORNER
        cur_x = new_x

# Wire 2
cur_x = 0
cur_y = 0
new_y = 0
new_x = 0
ans_x = []
ans_y = []
for i in range(0, len(wire2_dir)):
    if wire2_dir[i] == "U":
        new_y = cur_y - wire2_num[i]
        for y in range(cur_y-1, new_y, -1):
            try:
                if grid[y, cur_x] != NONE:
                    grid[y, cur_x] = INTERSECT
                    ans_x.append(cur_x)
                    ans_y.append(y)
                else:
                    grid[y, cur_x] = UP2
            except KeyError:
                grid[y, cur_x] = UP2
        grid[new_y, cur_x] = CORNER2
        cur_y = new_y
    if wire2_dir[i] == "D":
        new_y = cur_y + wire2_num[i]
        for y in range(cur_y+1, new_y):
            try:
                if grid[y, cur_x] != NONE:
                    grid[y, cur_x] = INTERSECT
                    ans_x.append(cur_x)
                    ans_y.append(y)
                else:
                    grid[y, cur_x] = UP2
            except KeyError:
                grid[y, cur_x] = UP2
        grid[new_y, cur_x] = CORNER2
        cur_y = new_y
    if wire2_dir[i] == "R":
        new_x = cur_x + wire2_num[i]
        for x in range(cur_x+1, new_x):
            try:
                if grid[cur_y, x] != NONE:
                    grid[cur_y, x] = INTERSECT
                    ans_x.append(x)
                    ans_y.append(cur_y)
                else:
                    grid[cur_y, x] = ACROSS2
            except KeyError:
                grid[cur_y, x] = ACROSS2
        grid[cur_y, new_x] = CORNER2
        cur_x = new_x
    if wire2_dir[i] == "L":
        new_x = cur_x - wire2_num[i]
        for x in range(cur_x-1, new_x, -1):
            try:
                if grid[cur_y, x] != NONE:
                    grid[cur_y, x] = INTERSECT
                    ans_x.append(x)
                    ans_y.append(cur_y)
                else:
                    grid[cur_y, x] = ACROSS2
            except KeyError:
                grid[cur_y, x] = ACROSS2
        grid[cur_y, new_x] = CORNER2
        cur_x = new_x

man_dist = []
for a in range(0, len(ans_x)):
    man_dist.append( abs(ans_x[a]) + abs(ans_y[a]))

print("Part 1: " + str(min(man_dist)))  # Correct!

