start_num = 108457
end_num = 562041
num = start_num
pass_count = 0

for num in range(start_num, end_num + 1):
    dig1 = int(str(num)[0:1])
    dig2 = int(str(num)[1:2])
    dig3 = int(str(num)[2:3])
    dig4 = int(str(num)[3:4])
    dig5 = int(str(num)[4:5])
    dig6 = int(str(num)[5:6])
    if dig1 <= dig2 and dig2 <= dig3 and dig3 <= dig4 and dig4 <= dig5 and dig5 <= dig6:
        if dig1 == dig2 or dig2 == dig3 or dig3 == dig4 or dig4 == dig5 or dig5 == dig6:
            pass_count += 1

print "Part 1: " + str(pass_count) # Correct!

