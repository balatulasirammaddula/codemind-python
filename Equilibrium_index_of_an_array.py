t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        a=r=0
        for j in range(i):
            a+=l[j]
        for k in range(i+1,n):
            r+=l[k]
        if r==a:
            print(i)
            break
    else:
        print(-1)