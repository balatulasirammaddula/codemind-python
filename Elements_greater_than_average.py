n=int(input())
l=list(map(int,input().split()))
s=c=0
for i in l:
    s+=i
av=s//n
for i in l:
    if i>=av:
        c+=1
print(c)        
