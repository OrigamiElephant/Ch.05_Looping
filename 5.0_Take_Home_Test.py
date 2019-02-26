'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Ezra McCulley
 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total = 0
answer = 0
for i in range(3):
    x = int(input("Enter a number: "))
    answer = answer + x
    total = total + i
print("The total is:", answer)
print()



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
x = 2
for i in range(50):
    print(x)
    x += 2
print()

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
x = 1
b = 10
while x == 1:
    print(b)
    b -= 1
    if b == -1:
        x = 0
print("Blast off!")
print()

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
x = random.randint(1,10)
print(x)
print()





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the number entries equal to zero,
     and the number of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
y = 0
p = 0
n = 0
z = 0
print("Please type seven numbers")
for i in range(7):
    x = int(input("Number:"))
    y += x
    if x > 0:
        p += 1
    elif x < 0:
        n += 1
    else:
        z += 1
print()
print("Total:",y)
print("Positives:",p)
print("Negatives:",n)
print("Zeros:",z)