'''
Functions with for loops
Question 1:
Write a function called count_even(numbers) that:

takes a list of integers as input

uses a for loop
returns the number of even values in the list
'''
#my solution

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

"""
Question 2:

Write a function called sum_positive(numbers) that:

takes a list of integers

uses a for loop

returns the sum of only the positive numbers (ignore negatives)
"""

#my answer
def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total


"""
n 3:

Write a function called find_max(numbers) that:

takes a list of integers

uses a for loop

returns the largest number in the list

❌ You are NOT allowed to use max()n 3:

Write a function called find_max(numbers) that:

takes a list of integers

uses a for loop

returns the largest number in the list

❌ You are NOT allowed to use max()
"""

#my answer
def find_max(numbers):
    largest = numbers[0] 

    for num in numbers:
        if num > largest:
            largest = num
            
    return largest
"""
Question 4:

Write a function called reverse_list(items) that:

takes a list

uses a for loop

returns a new list reversed

❌ You are NOT allowed to use [::-1]
"""
def reverse_list(items):
    reversed_items = []
    
    for item in items:
        
        return reversed_items

#correct answer
def reverse_list(items):
    reversed_items = []
    
    for item in items:
        reversed_items.insert(0, item)#where my mistake lies
        
    return reversed_items
"""
explanation:

reversed_items.insert(0, item)
insert(position, value) puts the value at a specific position in the list.

0 means the beginning of the list.

So every time the loop runs, the current item is placed at the front.

This pushes older items forward, gradually reversing the order.

reversed_items.insert(0, item)
insert(position, value) puts the value at a specific position in the list.

0 means the beginning of the list.

So every time the loop runs, the current item is placed at the front.

This pushes older items forward, gradually reversing the order.


simpler method

def reverse_list(items):
    reversed_items = []
    
    for i in range(len(items)-1, -1, -1):
        reversed_items.append(items[i])
        
    return reversed_items
"""

#While loop Questions


"""
Write a function countdown(n) that:

uses a while loop

prints numbers from n down to 1.
"""

#my answer
def countdown(n):
    while n > 0:
        print(n)
        n -= 1


'''
While Loop Question 2

Write a function called sum_until_zero() that:

repeatedly asks the user to enter numbers

uses a while loop

stops when the user enters 0

returns the sum of all entered numbers (excluding the final 0)
'''

#my answer
def sum_until_zero():
    total = 0
    number = int(input("Enter a number (0 to stop): "))
    
    while number != 0:
        total += number
        number = int(input("Enter a number (0 to stop): "))
        
    return total


"""
While Loop Question 3

Write a function factorial(n) that:

uses a while loop

calculates the factorial of n (n!)

example: factorial(5) → 120
"""
#my answer

def factorial(n):
    result = 1
    
    while n > 0:
        result *= n
        n -= 1
        
    return result
