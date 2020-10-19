"""
9.4 Write a program to read through
the mbox-short.txt and figure out who has
sent the greatest number of mail messages.
The program looks for 'From ' lines and takes
the second word of those lines as the person
 who sent the mail.
 The program creates a Python dictionary
  that maps the sender's mail address to a
  count of the number of times they appear
in the file. After the dictionary is produced,
 the program reads through the
 dictionary using a maximum loop
 to find the most prolific committer.
"""

l = list()
fname = input("Enter file name: ")
try :
    f = open(fname)

except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in f:
    if not line.startswith('From '): continue
    line=line.split()
    l.append(line[1])

d = dict()

for word in l:
    d[word]=d.get(word,0)+1

bigcount = None
bigword = None
for w,count in d.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = w

print (bigword,bigcount)
