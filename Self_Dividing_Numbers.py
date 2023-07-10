a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    s=str(temp)
    s=len(s)
    c=0
    while i>0:
        r=i%10
        if r==0:
            pass
        elif temp%r==0:
            c+=1
        i=i//10
    if s==c:
        print(temp,end=' ')