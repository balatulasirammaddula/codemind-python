n=int(input())
t=n
s=0
l=len(str(n))
while n>0:
    r=n%10
    s+=r**l
    n=n//10
    l=l-1
print(s==t)    