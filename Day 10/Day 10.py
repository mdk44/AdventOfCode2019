import math

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

def get_angles(points, origin):
    angles = dict()
    for point in points:
        if point == origin:
            continue
        else:
            angles[origin.get_angle(point)] = True
    return len(angles)

def get_highest(lines):
    maxm = 0
    points = make_points(lines)
    for point in points:
        count = get_angles(points, point)
        if count > maxm:
            maxm = count
    return maxm

print("Part 1: " + str(get_highest(lines))) # Correct!