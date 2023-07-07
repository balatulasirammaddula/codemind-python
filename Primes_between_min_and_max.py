def prime(n):
    is_prime=True
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
    return is_prime
n=int(input())
a=list(map(int,input().split()))
mi=min(a)
mx=max(a)
mini=min(a.index(mi),a.index(mx))
maxi=max(a.index(mi),a.index(mx))
cnt=0
for i in range(mini,maxi+1):
    if prime(a[i])==True:
        cnt+=1
print(cnt)