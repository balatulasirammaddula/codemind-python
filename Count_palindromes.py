def pal(n):
    n=str(n)
    s=n[::-1]
    if s==n:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if pal(l[i]):
        c+=1
print(c)    