def amicable(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
if amicable(n)==amicable(m):
    print('Amicable')
else:
    print('Not Amicable')