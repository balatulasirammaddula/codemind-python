n=int(input())
s=0
for i in range(1,n+1):
    if i*i==n:
        s=True
    else:
        pass
if s==True:
    print('True')
else:
    print('False')