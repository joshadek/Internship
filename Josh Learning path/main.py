def main():
    print("Hello from josh-learning-path!")

main()
'''x=1
print(x)
x=2+1
print(x)'''

#reserved words: Assigned functions and commands eg. if, while, false, for


"""if x>10:
    print("greater")
if x<10:
    print("lesser")
nj,b

x=5
if x>2:
    print("greater")
if x<8:
    print("lesser")
"""

'''y=10
while y>0:
    print(y)
    y=y-1
print("Complete")'''



'''name=input("Enter File Name: ")
handle=open(name, "r")

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word

print(bigword,bigcount)'''


#Lesson on constants, variable names and assignment


#Use of Mneumonic naming for variables is for humans to understand what the code is talking about
#Python doesnt know the meaning of variable names, neither does it care. It treats them all the same
'''
x=0.6
x=3.9*x*(1-x)
print(x)

'''

"""
Numeric expresssions:

**=raise to  power
%=remainder
"""
#use of modulo/remainder and raise to power operations
n=34
m=n%5
print(m)
print(4 ** m)

#demonstration of operator precedence
x=1+(2*3)-(4/(5**6)) #parenthesis is used for human discernment
#parenthesis > raised to power > division/multiplication/remainder > addition/subtraction(left to right)
print(x)