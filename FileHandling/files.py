

# open a file using open()
# you can use w,r,+
 # "W" can create a file it does not exist
f = open("trades.csv", "w") 
f.write("Hello")
f.close()

# you can read file with the "r"
f = open("trades.csv", "r")
f.read()   #  output = "Hello"
 

# if you open a file and "w" you will delete all the data
f = open("trades.csv", "w")
f.write("Good Bye")
f.close()
f = open("trades.csv", "r")
f.read()  # output = "Good Bye"

# write on multiple lines
f = open("trades.csv", "w")
f.write("Hello")   # make sure you put a \n to separate the lines
f.write("Good bye")
f.close()
f = open("trades.csv", "r")
f.read() 

# for sequence data type use readline and writeline
l = ('Hello', '\nGood Bye')
f = open('trades.txt', 'w')
f.writelines(l)
f.close()
f = open('trades.txt','r')
print(f.readline())  # reads only one line
f.close()

# readline for every entry in sequence
l = ('Hello', '\nGood Bye')
f = open('trades.txt', 'w')
f.writelines(l)
f.close()
f = open('trades.txt','r')
print(f.readline())  # reads only one line
print(f.readline())
f.close()

# use end = "" - to stop newline
l = ('Hello', '\nGood Bye')
f = open('trades.txt', 'w')
f.writelines(l)
f.close()
f = open('trades.txt','r')
print(f.readline(), end='')  # reads only one line
print(f.readline(), end='')
f.close()

# readlines and writelines
l = ('Hello', '\nGood Bye')
f = open('trades.txt', 'w')
f.writelines(l)
f.close()
f = open('trades.txt','r')
print(f.readlines())  # reads all the sequence
f.close()

# readline for every entry in sequence
f = open('trades.txt','r')
while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data, end='')
f.close()

# using Content Manager 'with' automatically closes file
with open('trades.txt', 'r') as f:
    print(f.read())

# adding data to file with 'a'
with open('trades.txt', 'a') as f:
    f.write('\nForever')
with open('trades.txt', 'r') as f:
    print(f.read())

# working wity csv 
import csv

with open('trades.csv', 'w', newline='') as f:
    writer = csv.writer(f)  # calling csv.writer to write to a csv file
    writer.writerow(["Symbol", "Price", "Quantity"])
    writer.writerow(["AAPL", "100", "10"])
    writer.writerow(["MSFT", "50", "20"])

with open('trades.csv', 'r') as f:
    tradereader = csv.reader(f)
    for row in tradereader:
        print(row)
