S=input('Write the word to check... \n')
i=0
n=len(S)
s=[]
while i<n:
    s.append(S[n-i-1])
    if s[i]!=S[i]:
        print(S+' is not a palindrome')
        break
    i+=1
if i==n:
    print(S+' is a palindrome')
