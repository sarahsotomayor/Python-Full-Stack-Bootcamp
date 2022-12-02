# Print all integers from 0 to 150.
for i in range(151):
    print (i)

# Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print (i)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(101):
    print (i)
    if i%5 == 0:
        print ("Coding")
    if i%10 == 0:
        print ("Coding Dojo")

#Add odd integers from 0 to 500,000, and print the final sum.
odd_total=0
for number in range(1,500000):
    if(number%2!=0):
        odd_total=odd_total+number
    if(number==5000000):
        break
print(odd_total)

#Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)

# Flexible Counter 
"""
Set three variables: lowNum, highNum, mult. Starting at lowNum and 
going through highNum, print only the integers that are a multiple of mult. For example, if 
lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""
lowNum = 10
highNum = 32
mult = 5
for i in range(lowNum, highNum):
    if i%mult==0:
        print(i)

