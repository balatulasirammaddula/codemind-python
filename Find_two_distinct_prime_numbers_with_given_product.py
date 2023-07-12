def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n):
    if prime(i):
        for j in range(1,n):
            if i*j==n:
                print(i,j)
                c=1
                break
        if c==1:
            break
if c==0:
    print(-1)
        
        