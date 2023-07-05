n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=cnt=0
for i in range(n):
    if l[i]<a or l[i]>b:
        cnt=1
        if l[i]>s:
            s=l[i]
if cnt==0:
    print(-1)
else:
    print(s)
        
        