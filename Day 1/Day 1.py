input_file = 'Day 1\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split()

# Part 1
sum = 0
for line in lines:
    cur_wt = int(int(line) / 3) - 2
    sum += cur_wt

print sum