def fact(n):
    if n==0:
        return 1
    if n == 1:
        return n
    else:
        return n*fact(n-1)
n=int(input())
t=n
s=0
while n>0:
    r=n%10
    s=fact(r)+s
    n=n//10
if s==t:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')