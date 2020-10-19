
import re
#open file
f = open("regex_sum_998845.txt")

x=list()
for line in f:
    #find all numbers
     y = re.findall('[0-9]+',line)
     #sum lists
     x = x+y

sum=0
for number in x:
    sum = sum + int(number)

print(sum)
