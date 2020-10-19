""" Write a program that prompts for a file name,
then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values
 from each of the lines and compute the average of those values
  and produce an output as shown below.
   Do not use the sum() function or a variable
    named sum in your solution. """

fname = input("Enter file name: ")
counter = 0
total = 0
try :
    f = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for word in f:
     if not word.startswith("X-DSPAM-Confidence:") : continue
     counter = counter +1
     temp = word.find('0')
     num = float(word[temp:])
     total = total +num

promedio = float(total/counter)
print ("Average spam confidence:",average)
