# key facts about the password:


# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 108457-562041.

start_num = 108457
end_num = 562041
num = start_num
pass_count = 0
test = 112345

for num in range(start_num, end_num + 1):
    dig1 = int(str(num)[0:1])
    dig2 = int(str(num)[1:2])
    dig3 = int(str(num)[2:3])
    dig4 = int(str(num)[3:4])
    dig5 = int(str(num)[4:5])
    dig6 = int(str(num)[5:6])
