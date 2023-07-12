n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if a[i] not in l:
        l.append(a[i])
c=[]
for i in range(len(l)):
    if l[i]==a.count(l[i]):
        c.append(l[i])
if c==[]:
    print(-1)
else:
    mx=max(c)
    mn=min(c)
    print(mn,mx,sep=' ')