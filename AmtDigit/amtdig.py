# How many digit in #
number = 1923347655123

digit_amount = len(str(number))
print(digit_amount)

# non typecast - wont work when 0
import math

number = -1102    #1923347655123

if number > 0:
    print(int(math.log10(number))+1)
elif number < 0:
    print(int(math.log10(-number))+1)
else:
    print('1')

# PC cant accurately rep floats - so if you use log10 with a lot of digits you get errors

number = 999999999999999999997
# this is accurate
print(len(str(number)))
# Log10 will not be accurate, it round up creating an extra digit
if number > 0:
    print(int(math.log10(number))+1)
elif number < 0:
    print(int(math.log10(-number))+1)
else:
    print('1')

# use a counter
number =  -2123   #999999999999999999997
# when you have a '-' it is counted as 1 so be carefull
if '-' in str(number):
    print(len(str(number)) - 1)
else:
    print(len(str(number)))

counter = 1

while abs(number) >= (10 ** counter):
    counter += 1
print(counter)


