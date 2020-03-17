#user input
N=int(input('How many Fibonacci numbers do you want generate? '))
F=[1,1]
i=2 #actually len(F)
if N>2:
    while i<N:
        nxt=sum(F[i-2:])    #calculate next number = sum of the last two elements
        F.append(nxt)       #append it
        i+=1                #i=len(F)
print(F)
