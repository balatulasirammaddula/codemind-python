x=int(input())
for _ in range(x):
    h=int(input())
    n=h
    p=h
    while True:
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime==True:
            t=n
            break
        n+=1
    while True:
        is_prime=True
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                is_prime=False
                break
        if is_prime==True:
            m=p
            break
        p-=1
    u=abs(h-t)
    y=abs(h-m)
    if u<y:     
        print(t)
    elif u>y:
        print(m)
    else:
        print(min(t,m))