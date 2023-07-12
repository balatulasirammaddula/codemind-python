def pro(n):
    for i in range(1,n+1):
        if i*(i+1)==n:
            return True
            break
    return False
n=int(input())
if pro(n)==True:
    print('YES')
else:
    print('NO')