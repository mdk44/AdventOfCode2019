input_file = 'Day 8\\Input.csv'
text_file = open(input_file)
lines = [int(line) for line in text_file.read()]

# 0 - 24
# 25 - 49
# 50 - 74
# 75 - 99
# 100 - 124

start_num = 0
count_0 = 0
count_1 = 0
count_2 = 0
num_0 = 20000
num_1 = 0
num_2 = 0

for i in range(start_num, start_num + 125):
    if lines[i] == 0:
        count_0 += 1
    elif lines[i] == 1:
        count_1 += 1
    elif lines[i] == 2:
        count_2 += 1
if count_0 < num_0:
    num_0 = count_0
    num_1 = count_1
    num_2 = count_2
    print "0: " + str(num_0) + "  1x2: " + str(num_1 * num_2)