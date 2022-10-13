a=int(input())
b=int(input())
s1=0
s2=0
for i in range (1,a+1):
    if a%i==0:
        s1+=i
for i in range(1,b+1):
    if b%i==0:
        s2+=i
if s1==s2 or s2==s1:
    print('Amicable')
else:
    print('Not Amicable')

