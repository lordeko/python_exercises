#check_palindrome is the same of palindrome.py
#actually this code trasnform a sentence in a unique word (whitout spaces) and check the condition

def check_palindrome(S):
    i=0
    n=len(S)
    s=[]
    while i<n:
        s.append(S[n-i-1])
        if s[i]!=S[i]:
            return 0
            break
        i+=1
    if i==n:
        return 1

#main
S=input('Write the sentence to check... \n')

m=S.count(' ') # number of spaces in S
if m==0:
    flag=check_palindrome(S) #it's a word, no need to transform it
else:
    i=0
    n=len(S)
    S2=[]
    while i<n:
        if S[i]!=' ':      #if S[i] is a space, skip it
            S2.append(S[i])
        i+=1
    flag=check_palindrome(S2) #check the new "nospace" string
#output with the original string S
if flag:
    print(S+' is a palindrome')
else:
    print(S+' is not a palindrome')
