'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''

import random
i = 1
camel = 0
canteen = 3
miles = 0
natives = -10
thirst = 0
oasis = 0
while i == 1:
    oasis = random.randint(1,20)
    if oasis == 1:
        print("You found an oasis")
        camel = 0
        thirst = 0
        canteen = 3
        print()
    if thirst > 3:
        print("You are thirsty")
    if camel > 5:
        print("Your camel is tired")
    print("The natives are", miles - natives, "Miles behind you")
    print("What would you like to do?")
    print("A.Drink")
    print("B.Moderate Speed")
    print("C.Full Speed")
    print("D.Stop")
    print("E.Status")
    print("Q.Quit")
    x = input("Enter Letter:")
    o = random.randint(1, 20)  # random generator for oasis
    print()

    if x.upper() == "A":  # Canteen chances and numbers
        o = 0
        if canteen > 0:
            canteen -=1
            thirst = 0
            a = random.randint(1,10)
            if a == 1:
                print("You drink out of your canteen, tastes like gasoline")
            elif a == 2:
                print("You drink out of your canteen, tastes like paint")
            elif a == 3:
                print("You drink out of your canteen, tastes like hydrochloric acid")
            else:
                print("You drink out of your canteen.")
        elif canteen == 0:
            print("You drink in refreshing nothingness, it's empty")

    elif x.upper() == "B":  # Moderate speed numbers
        b = random.randint(1,10)
        camel += 1
        miles += random.randint(5, 12)
        natives += random.randint(7,14)
        thirst += 1
        if b == 1:
            print("You fall off the camel but are dragged behind by a rope tied to your foot")
        elif b == 2:
            print("Your camel lifts itself off the ground and begins to hover forward")
        elif b == 3:
            print("You end up carrying your camel for a few miles")
        else:
            print("You move at a reasonable pace")
        print("You moved", miles, "miles total")

    elif x.upper() == "C":  # Fast speed numbers
        c = random.randint(1,10)
        camel += random.randint(1,3)
        miles += random.randint(10, 20)
        natives += random.randint(7,14)
        thirst += 1
        if c == 1:
            print("You move at a godlike speed for a fraction of a second")
        elif c == 2:
            print("You teleport in the direction you were walking")
        elif c == 3:
            print("You pass out and wake up further along the path")
        else:
            print("You walk at a faster pace")
        print("You moved", miles, "miles total")

    elif x.upper() == "D":  # Stopping numbers
        o = 0
        d = random.randint(1,10)
        natives += random.randint(7, 14)
        camel = 0
        if d == 1:
            print("You and your camel freeze in  time for a while and feel refreshed afterwards")
        elif d == 2:
            print("You enter the fourth dimension while you stop and rest up")
        elif d == 3:
            print("Your camel disappears for a little while, but later appears again wearing a sombrero")
        else:
            print("You stop and rest")

    elif x.upper() == "E":  # Status Numbers
        print("Your canteen has", canteen, "drinks left")
        print("You moved", miles, "miles total")
        print("Your camel has", 7 - camel, "days left")

    elif x.upper() == "Q":  # Quitter
        q = random.randint(1,10)
        if q == 1:
            print("You give up all hope and fall face first into the sand, accepting your fate")
        elif q == 2:
            print("You are  picked up by a large vulture who takes you back to its nest and raises you s its own")
        elif q == 3:
            print("You black out and wake up in a horse drawn cart. A man across from you says,")
            print("Oh. your finally awake")
    if o == 1:
        print()
        print("You find an oasis")
        thirst = 0
        camel = 0
        canteen = 3
    if thirst > 4 or natives >= miles or camel > 6 or miles >= 200:  # Game ending variables
        i = 0
    print()

print()
if miles >= 200:
    aa = random.randint(1,6)
    if aa == 1:
        print("You survived, you made it to a town.")
        print("The only business you see is a camel shop.")
    elif aa == 2:
        print("You find a town that treats outsiders with the utmost respect and luxury.")
        print("Outsiders being camels. You end up drinking out of a water pump.")
    elif aa == 3:
        print("You return to the town you first traveled from. You see your wife and kids walking towards you.")
        print("Unfortunately you remember that it's your ex-wife as well as why you put yourself out in the desert.")
    else:
        print("You make it back to town and you and your camel have a nice cold drink.")
elif thirst > 4:
    if canteen > 0:
        print("You die from dehydration, even though you still had water in your canteen.")
        print("Your camel drinks the rest of the water from the canteen to spite you.")
    else:
        ab = random.randint(1, 6)
        if ab == 1:
            print("Your canteen getting tired of not being properly filled or drank out of fills itself with sand.")
            print("you die of thirst because you didn't love and care for your canteen.")
        elif ab == 2:
            print("Due to lack of water your body dries up completely, leaving a dry husk of a person on the ground")
        elif ab == 3:
            print("Your canteen miraculously fills with water, you feverishly drink from the canteen.")
            print("But as you keep drinking you find out it's actually th water from your body filling the canteen.")
            print("You keep drinking to try and keep it in but te canteen fills up faster than you can drink.")
        else:
            print("You die of thirst")
elif natives >= miles:
    ac = random.randint(1, 6)
    if ac == 1:
        print("Instead of eating you the natives poke you with a pointy stick. You don't know what was on it.")
        print("You now have HIV.")
    elif ac == 2:
        print("The natives take you back to their village, and worship you like a god.")
        print("Unfortunately they think you don't need to eat and you starve to death.")
    elif ac == 3:
        print("The natives feel bad about your camel, so they pull you off of it and take it with them.")
        print("Unfortunately this means you are left in the desert without a camel to ride.")
    else:
        print("The natives capture you amd you camel and they look famished")
elif camel >= 6:
    ad = random.randint(1, 6)
    if ad == 1:
        print("Your camel gets sick of carrying you around and prays to the sky god Zeus.")
        print("You are immediately struck by lightning as your camel is whisked off to olympus.")
    elif ad == 2:
        print("You here a loud, firm snap in the distance.")
        print("Your camel begins to disintegrate and turn into dust as the particles are swept away by the wind.")
    elif ad == 3:
        print("Your camel begins to shake rapidly until it implodes on itself, disappearing from existence")
    else:
        print("Your camel becomes too fatigued and dies from being over-worked")
else:
    print("How did you get here?")
    print("Well, You lose anyways.")
