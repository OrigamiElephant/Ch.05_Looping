'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
i = 1
miles = 0
canteen = 3
natives = 10
while i == 1:
    print("What would you like to do?")
    print("A.Drink")
    print("B.Moderate Speed")
    print("C.Full Speed")
    print("D.Stop")
    print("E.Status")
    print("Q.Quit")
    x = input("Enter Letter:")
    print()
    if x.upper() == "A": #Canteen chances and numbers
        canteen -=1
        a = random.randint(1,10)
        if a == 1:
            print("You drink out of your canteen, tastes like gasoline")
        elif a == 2:
            print("You drink out of your canteen, tastes like paint")
        elif a == 3:
            print("You drink out of your canteen, tastes like hydrochloric acid")
        else:
            print("You drink out of your canteen.")

    elif x.upper() == "B": #Moderate speed numbers
        b = random.randint(1,10)
        if b == 1:
            print("You fall off the camel but are dragged behind by a rope tied to your foot")
        elif b == 2:
            print("Your camel lifts itself off the ground and begins to hover forward")
        elif b == 3:
            print("You end up carrying your camel for a few miles")
        else:
            print("You move at a reasonable pace")

    elif x.upper() == "C": #Fast speed numbers
        c = random.randint(1,10)
        if c == 1:
            print("You move at a godlike speed for a fraction of a second")
        elif c == 2:
            print("You teleport in the direction you were walking")
        elif c == 3:
            print("You pass out and wake up further along the path")
        else:
            print("You walk at a faster pace")

    elif x.upper() == "D": #Stopping numbers
        d = random.randint(1,10)
        if d == 1:
            print("You and your camel freeze in  time for a while and feel refreshed afterwards")
        elif d == 2:
            print("You enter the fourth dimension while you stop and rest up")
        elif d == 3:
            print("Your camel disappears for a little while but later appears again wearing a sombrero and holding a maraca in its mouth")
        else:
            print("You stop and rest")

    elif x.upper() == "E": #Status Numbers
        print()

    elif x.upper() == "Q": #Quitter
        q = random.randint(1,10)
        if q == 1:
            print("You give up all hope and fall face first into the sand, accepting your fate")
        elif q == 2:
            print("You are  picked up by a large vulture who takes you back to its nest and raises you s its own")
        elif q == 3:
            print("You black out and wake up in a horse drawn cart. A man across from you says,")
            print("Oh. your finally awake")
    print()

