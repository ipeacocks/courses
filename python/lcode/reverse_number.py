x = -45445551234555120
str_x_list = []
sum = ""
minus_sym = False

import sys

for i in str(x):
    str_x_list.append(i)

if str_x_list[0] == '-':
    minus_sym = True
    str_x_list= str_x_list[1:]


if minus_sym:
    a = ['-'] + str_x_list[::-1]
else:
    a = str_x_list[::-1]


for i in a:
    sum = sum + i

x = int(sum)
# print(x)

print(sys.getsizeof(x))
if sys.getsizeof(x) < 32:
    print(x)
else:
    print(0)
