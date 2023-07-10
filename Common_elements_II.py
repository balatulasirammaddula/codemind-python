n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    if a[i] not in b:
        l.append(a[i])
for i in range(len(b)):
    if b[i] not in a:
        l.append(b[i])
for i in range(len(l)):
    print(l[i],end=' ')