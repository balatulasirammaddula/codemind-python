def prnt(n):
    temp=n
    cnt=0
    s=str(temp)
    l=len(s)
    while n>0:
        r=n%10
        if r==0:
            break
        elif temp%r==0:
            cnt+=1
        n=n//10
    if cnt==l:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prnt(i)==True:
        print(i,end=' ')