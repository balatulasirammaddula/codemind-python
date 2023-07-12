n=int(input())
a=list(map(int,input().split()))
c=int(input())
s=[]
for i in range(n):
    if a[i] not in s:
        s.append(a[i])
t=0        
for i in range(len(s)):
    if c==a.count(s[i]):
        print(s[i],end=' ')
        t=1
if t==0:
    print(-1)
        
    
        
        
    