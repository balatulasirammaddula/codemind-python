n=int(input())
l=list(map(int,input().split()))
s=set(l)
s=list(s)
for i in range(len(s)):
    print(s[i],end=' ')