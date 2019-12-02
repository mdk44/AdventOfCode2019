#Test data
# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99

input_file = 'Day 2\\Input.csv'
text_file = open(input_file)
lines = text_file.read()

input_text = '1,0,0,0,99'
input_text = '2,3,0,3,99'
input_text = '2,4,4,5,99,0'
input_text = '1,1,1,4,99,5,6,0,99'
