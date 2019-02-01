'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
h = 0
t = 0
import random
for x in range(50):
    c = (random.randint(0,1))
    if c == 1:
        print("Heads")
        h +=1
    else:
        print("Tails")
        t +=1
print("# of Heads:",h)
print("# of Tails:",t)









