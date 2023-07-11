a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    s+=i**0.5
print('{:.2f}'.format(s))    