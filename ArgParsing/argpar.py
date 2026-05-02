# passing args via *args and **kwargs
def myfunc(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs['one'])
    print(kwargs['two'])

myfunc(1, 2, one='one', two='two')


# Argument parsing
import sys

print(sys.argv)
print(sys.argv[0]) 
print(sys.argv[1])

# run this script from term - python argpar.py text
sys.arg[0] = 'argpar.py'
sys.arg[1] = 'text'
# sys.argv is a list of command-line arguments passed to the script. The first element (sys.argv[0]) is the name of the script itself, and the subsequent elements are the additional arguments provided by the user when running the script. 

# write command to a file
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)
# run this script from term - python argpar.py test.txt hello

# op args = optional arguments
# python argpar.py -p 8080 = -p means port and 8080 is the value of the port
# python argpar.py -h = -h means help and it will show the help message
# f: means that the -f option requires a value (the filename), and m: means that the -m option also requires a value (the message). The long options --filename and --message are equivalent to the short options -f and -m, respectively.
# m: means that the -m option requires a value (the message). The long options --filename and --message are equivalent to the short options -f and -m, respectively.

import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])
print(opts)
print(args)

# run - python argpar.py -f text.txt -m hello
# output = [('-f', 'text.txt'), ('-m', 'hello')]

import getopt
import sys

filename = "test.txt"
message = "Hello"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)
