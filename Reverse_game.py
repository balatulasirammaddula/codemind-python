def rev(n):
    n=str(n)
    return int(n[::-1])
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    print(rev(l[i]),end=' ')