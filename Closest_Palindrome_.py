def pali(n):
    n=str(n)
    if n==n[::-1]:
        return True
n=int(input())
np=1
pp=1
while True:
    if pali(n+np)==True:
        np=n+np
        break
    else:
        np+=1
while True:
    if pali(n-pp)==True:
        pp=n-pp
        break
    else:
        pp+=1
if abs(n-np)>abs(n-pp):
    print(pp)
elif abs(n-np)<abs(n-pp):
    print(np)
else:
    print(pp,np)

