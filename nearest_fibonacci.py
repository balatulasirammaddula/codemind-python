def fibs(n):
    if n==0:
        print(0)
        return
    f=0
    s=1
    t=s+f
    while t<=n:
        f=s
        s=t
        t=s+f
    if abs(t-n)>abs(s-n):
        print(s)
    elif abs(t-n)==abs(s-n):
        print(s,t)
    else:
        print(t)
n=int(input())
fibs(n)
