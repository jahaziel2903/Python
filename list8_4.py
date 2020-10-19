"""
Open the file romeo.txt and read it line by line.
 For each line, split the line into a list of words using the split()
 method. The program should build a list of words.
  For each word on each line check to see if the word is already
   in the list and if not append it to the list.
    When the program completes, sort and print the
     resulting words in alphabetical order.

"""
fname = input("Enter file name: ")
final = list()
try :
    f = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for word in f:
        pieces = word.rstrip().split()
        for x in pieces:
            if x in final : continue
            final.append(x)

final.sort()
print(final)
