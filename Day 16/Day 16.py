input_file = 'Day 16\\Input.csv'
# text_file = open(input_file)
text_file = '12345678'

lines = []
# for i in list(text_file.read()):
for i in list(text_file):
    lines.append(int(i))

base_pattern = [0,1,0,-1]