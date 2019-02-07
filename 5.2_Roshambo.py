'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
i = 1
p = 0
win = 0
tie = 0
lose = 0
while i == 1:
    n = input("Rock(1), Paper(2), Scissors(3), or quit(4)?")
    if n == "1":
        p = 1
    elif n == "2":
        p = 2
    elif n == "3":
        p = 3
    elif n == "4":
        p = 4
    else:
        print("Please input the number next to your choice")
    cpu = random.randint(1, 3)
    if cpu == 1:
        print("Rock")
    elif cpu == 2:
        print("paper")
    elif p == 4:
        print()
    else:
        print("Scissors")
    if cpu == p:
        print("Tie")
        tie += 1
    elif cpu == 1 and p == 2:
        print("Paper beats Rock. You Win")
        win += 1
    elif cpu == 1 and p == 3:
        print("Rock beats Scissors. You Lose")
        lose += 1
    elif cpu == 2 and p == 1:
        print("Paper beats Rock. You Lose")
        lose += 1
    elif cpu == 2 and p == 3:
        print("Scissors beat Paper. You win")
        win += 1
    elif cpu == 3 and p == 1:
        print("Rock beats Scissors. You Win")
        win += 1
    elif cpu == 3 and p == 2:
        print("Scissors beat Paper. You Lose")
        lose += 1
    elif p == 4:
        i = 0
else:
    print("Ties", tie)
    print("wins", win)
    print("Losses", lose)