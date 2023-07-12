n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if a[i] not in l:
        l.append(a[i])
c=0
for i in range(len(l)):
    if l[i]==a.count(l[i]):
        print(l[i],end=' ')
        c=1
if c==0:
    print('-1')