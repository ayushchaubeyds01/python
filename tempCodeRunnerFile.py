n=int(input("enter n:"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print("* ",end="")
  for k in range(2*(n-i)):
    print("  ",end="")
  for l in range(1,i+1):
    print("* ",end="")
  print()