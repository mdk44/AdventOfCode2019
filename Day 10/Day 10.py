import math
import itertools

# input_file = 'Day 10\\Test1.csv'
# input_file = 'Day 10\\Test2.csv'
# input_file = 'Day 10\\Test3.csv'
# input_file = 'Day 10\\Test4.csv'
# input_file = 'Day 10\\Test5.csv'
input_file = 'Day 10\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# NEED TO FIGURE OUT TYPE HINTS

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def get_angle(self, origin):
        angle = math.atan2(self.y - origin.y, self.x - origin.x) * 180 / math.pi
        if angle < 0:
            return angle + 360
        else:
            return angle

def make_points(lines):
    points = []
    for y in range(0,len(lines)):
        line = lines[y]
        for x in range(0,len(line)):
            if line[x] == "#":
                point = Point(x, y)
                points.append(point)
    return points

def get_angle_count(points, origin):
    angles = dict()
    for point in points:
        if point == origin:
            continue
        else:
            angles[origin.get_angle(point)] = True
    return len(angles)

def get_highest(lines):
    maxm = 0
    max_point = None
    points = make_points(lines)
    for point in points:
        count = get_angle_count(points, point)
        if count > maxm:
            maxm = count
            max_point = point
    return maxm, max_point

def get_angle_map(points, origin):
    angles = dict()
    for point in points:
        if point == origin:
            continue
        angle = origin.get_angle(point) - 90
        if angle < 0:
            angle += 360
        if angle not in angles:
            angles[angle] = []
        angles[angle].append(point)
    return angles


count, point = get_highest(lines)
print("Part 1: " + str(point) + ", " + str(count)) # Correct!

angle_map = get_angle_map(make_points(lines),point)
sort_item = sorted (angle_map.keys())

point = angle_map[sort_item[199]]

for pnt in point:
    print("Part 2: " + str(pnt.x * 100 + pnt.y))