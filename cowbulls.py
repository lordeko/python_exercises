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
    n.append(str(rnd.randint(0,9))) #random generate number and convert in string

#print(n) -> very useful for debug XD

g=[]
cnt=0
while g!=n:
    cnt+=1
    b=c=0
    g=input('guess the number (4-digits)').split() #input a string made by 4 digit (string format)
    print(g) #just tu check
    for i in range(4):
        if n[i]==g[i]: #in Python string is a list of char, amazing!
            c+=1       #count your cows
        else:
           # g(i) not eq n(i) -> if n contains more "g[i]", this g[i] is a bull
           # ex.:          n= 1 2 0 2 and g = 2 1 0 3
           # for i=0.....  n(0)=1!=2=g(0) -> BUT n contains two "2" and g(0) contains one "2" -> IS A BULL
           # for i=1.....  n(1)=2!=1=g(1) -> BUT n contains one "1" and g(0:1),remember python exclude right element, contains one "1" -> IS A BULL
            if n.count(g[i])>g[:i].count(g[i]): 
                b+=1
    print(f'You have {b} bulls and {c} cows... try again!')
print(f'WHOA!YOU DID IT! You used {cnt} guesses')
