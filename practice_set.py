# ##even odd
# num=int(input("enter n:"))
# print("even" if num%2==0 else "odd")


# ##greatest of 3 numbers
# num1=int(input("enter n:"))
# num2=int(input("enter n:"))
# num3=int(input("enter n:"))
# if num1>num2 and num1>num3:
#     print("num1 is greatest")
# elif(num2>num3 and num2>num1):
#     print("num2 is greatest")
# else:
#     print("nyum3 is greatest")
    
    
# ##leap year checker
# year=int(input("enter year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")
    
    
    
    
# #simple calculator
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# op=input("enter operator (+,-,*,/): ")
# match op:
#     case "+":
#         print("sum:", a+b)
#     case "-":
#         print("subtraction:", a-b)
#     case "*":
#         print("multiplication:", a*b)
#     case "/":
#         print("division:", a/b)
#     case _:
#         print("invalid operator")
        


# ##positive negative 0
# num=int(input("Enter n:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("0")
    

# ##grade calculator
# marks = int(input("Enter marks: "))
# match marks // 10:
#     case 10 | 9:
#         print("Grade: A")
#     case 8:
#         print("Grade: B")
#     case 7:
#         print("Grade: C")
#     case 6:
#         print("Grade: D")
#     case _:
#         print("Grade: F")
        






###  loops

# #  print numbers 1 to n
n=int(input("enter  n:"))
for i in range(1,n+1):
    print(i)


# # sum of digits
n=int(input("enter  n:"))
sum=0
while n>0:
    sum+=(n%10)
    n//=10
print(sum)


# # fibonacci series
n=int(input("enter  n:"))
a,b=0,1
for i in range(1,n+1):
    print(a)
    a,b=b,a+b



# # factorial of number
n=int(input("enter  n:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


# prime number 
n=int(input("enter  n:"))
if n<2:
    print("not prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
        