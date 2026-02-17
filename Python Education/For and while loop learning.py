#For loop lessons

for i in range(1, 6):
    print(i)


for i in range(3):
    print("Hello")
 

for i in range(3):
    print(i)

print("--") #This is just a separator




#Loop using something internal
for something in range(3):
    print(something)



#Looping through lists
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)





#using steps
for i in range(0, 10, 2):
    print(i)
#range(start,stop,step)



#for loop using break
for i in range(1, 10):
    if i==5:
        break
    print(i)

    
#for loop using continue
for i in range(1, 6):
    if i==3:
        continue
    print(i)

    
    




#While loop lessons


counter=0
while counter<4:
  print(counter)
  counter=counter+1

    
seats=500 #initial number/counter
#counters also help avoid infinite loops
while seats>0: #available seats?
    print("Sell Tickets") #tickets sold
    seats= seats-1 #updated number of seats




i=1
while i<=5:
    print(i)
    i += 1


#user input loop
password=""
while password !="1234":
    password=input("Enter password: ")
    
    print ("Access granted")















    
