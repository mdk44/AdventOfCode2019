input_file = 'Day 1\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split()

# Part 1
sum_p1 = 0
for line in lines:
    cur_wt = int(int(line) / 3) - 2
    sum_p1 += cur_wt

print "Sum for Part 1: " + str(sum_p1)

sum_p2 = 0
for line in lines:
    cur_wt = int(line)
    while cur_wt > 0:
        cur_wt = int(cur_wt / 3) - 2
        if cur_wt > 0:
            sum_p2 += cur_wt

print "Sum for Part 2: " + str(sum_p2)