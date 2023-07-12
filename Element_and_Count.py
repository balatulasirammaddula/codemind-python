n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if a[i] not in l:
        l.append(a[i])
for i in range(len(l)):
    print(l[i],a.count(l[i]),end=' ')