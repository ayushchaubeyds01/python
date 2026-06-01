a=int(input(("enter a:")))
n=int(input(("enter n:")))
r=int(input(("enter r:")))
sum=0
for i in range(a,n+1):
    sum+=a
    a=a*r
print(sum)