input_file = 'Day 8\\Input.csv'
text_file = open(input_file)
lines = [int(line) for line in text_file.read()]

# 0 - 24
# 25 - 49
# 50 - 74
# 75 - 99
# 100 - 124

start_num = 0
count_zero = 0
num_1 = 0
num_2 = 0

for i in range(start_num, start_num + 125):
    print i