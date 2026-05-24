#palindrome no
n=int(input("enter n:"))
b=str(n)
rev=0
for i in range (1,len(b)+1):
    rev=rev*10+n%10
    n//=10
if (rev==n):
    print("it is a palindrome")
else:
    print("it is not a palindrome")