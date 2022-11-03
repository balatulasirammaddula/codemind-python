def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return True
    return False
n=int(input())
if palindrome(n)==True:
    print('True')
else:
    print('False')
                