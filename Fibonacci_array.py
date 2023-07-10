n=int(input())
a=list(map(int,input().split()))
c=0
if n<=2:
    print('no')
else:
    for i in range(2,n):
        if a[i-1]+a[i-2]==a[i]:
            pass
        else:
            c=1
    if c==0:
        print('yes')
    else:
        print('no')