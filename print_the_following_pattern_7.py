n=int(input())
for i in range(n):
    for k in range(1,n-1):
        print(k,end='')
    for j in range(1,n-2):
        print(j,end='')
    print()    