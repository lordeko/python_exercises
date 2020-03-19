#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number.
#Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place,
#they have a “cow”.
#For every digit the user guessed correctly in the wrong place is a “bull.”
#Every time the user makes a guess, tell them how many “cows”
#and “bulls” they have.
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random as rnd

n=[]
for i in range(4):
    n.append(str(rnd.randint(0,9)))

#print(n)

g=[]
cnt=0
while g!=n:
    cnt+=1
    b=c=0
    g=input('guess the number (4-digits)').split()
    print(g)
    for i in range(4):
        if n[i]==g[i]:
            c+=1
        else:
            if n.count(g[i])>g[:i].count(g[i]):
                b+=1
    print(f'You have {b} bulls and {c} cows... try again!')
print(f'WHOA!YOU DID IT! You used {cnt} guesses')
