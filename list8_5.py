"""
Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split()
and print out the second word in the line
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.

Hint: make sure not to include the
lines that start with 'From:'.
Also look at the last line of the sample
output to see how to print the count.
mbox-short.txt

"""
fname = input("Enter file name: ")
count = 0

try :
    f = open(fname)

except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in f:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1


print("There were", count, "lines in the file with From as the first word")
