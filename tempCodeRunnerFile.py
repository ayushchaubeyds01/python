
*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
'''

n=int(input("enter n:"))
for  i in range(1,n+1):
  print("* "*i)
for j in range(n-1,0,-1):
  print("* "*j)
for k in range(1,i+1):
  for l in range(n-i):
    print("  ",end="")
  for m in range(1,k+1):
    print("* ",end="")
  print()