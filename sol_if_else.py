# import math
# num=int(input("enter a no:"))
# root=math.sqrt(num)
# if(num==root**2) and not (num==root**3):
#     print("it is not a cube")
# else:
#     print("unsatisfied condition")


# num=int(input("enter a no"))
# if(num%3==0 or num%5==0 and not num%3==0 and num%5==0):
#     print("number is divisible by either 3 or 5 but not both")
# else:
#     print("unsatisfied condition")

# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# num3=int(input("enter a number:"))
# num4=int(input("enter a number:"))
# if(num1>num2 and num1>num3 and num1>num4):
#     print("num1 is greater")
# elif(num2>num1 and num1>num3 and num1>num4):
#     print("num2 is greater")
# elif(num3>num2 and num1>num1 and num1>num4):
#     print("num3 is greater")
# elif(num4>num2 and num1>num3 and num1>num1):
#     print("num4 is greater")
# else:
#     print("unsatisfied condition")
    
    
# year=int(input("enter a no:"))
# if(year%4==0):
#     print("leap year")
#     if(year%400==0 and  (year%1000!=0)):
#         print("divisble by 400 not by 1000")
# else:
#     print("unsatisfied condition")


# side1=int(input("enter a number:"))
# side2=int(input("enter a number:"))
# side3=int(input("enter a number:"))
# if(side1+side2>side3 and( (side1**2) + (side2**2)==(side3**2))):
#     print("it is a right angled triangle")

# num=int(input("enter a no:"))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10
# print(sum)
# if(num%sum==0):
#     print("it is harshad no")
# else:
#     print("not")

# num=int(input("enter a no:"))
# if(10<num<50 or 100<num<150):
#     print("number lies between two ranges (10–50 OR 100–150)")
# else:
#     print("not")



# num=int(input("enter a no:"))
# square=num**2
# temp=square
# while temp>len(str(square)):
#     digit=temp%10
#     if(digit==num):
#         print("it is automorphic no")
#     else:
#         print("not")
#     break



# num=int(input("Enter a no:"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
#     else:
#         pass
# if(sum==num and num%2==0):
#     print("it is perfect no and is even")
# else:
#     print("not")


# temprature=float(input("Enter temprature:"))
# if(temprature==0):
#     print("freezing point")
# elif(0<temprature<100):
#     print("normal")
# else:
#     print("boiling")


# password="Satyam@@123"
# while True:
#      enter_pass=str(input("enter password:"))
#      if(enter_pass==password):
#          print("unlocked")
#          break
#      else:
#          print("try again")   

# vowel='a','e','i','o','u'
# special_char="@!#$%^&*"
# enter=input("enter to check:")
# if(enter in vowel):
#     print("it is vowel")
# elif(enter not in vowel and not enter.isdigit()):
#     print("it is a consonent")
# elif(enter in special_char):
#     print("it is a special charector")
# elif(enter.isdigit()):
#     print("it is a digit")
# else:
#     print("unsatisfied condition")


# num=int(input("enter number:"))
# if(num<0 and num%2==0):
#     print('num is negative and is even ')
# elif(num==0):
#     print("num is zero")
# elif(num>0 and num%2==0):
#     print("num is positive and is even")
# elif(num%2!=0):
#     print("odd")
# else:
#     print("unsatisfied condition")


# marks=int(input("Enter marks:"))
# if(marks>90):
#     print("A++")
# elif(70<marks<90):
#     print("A")
# elif(45<marks<70):
#     print("B")
# else:
#     print("fail")


# num1=int(input("enter no:"))
# num2=int(input("enter no:"))
# num3=int(input("enter no:"))
# if(num1<num2 and num1<num3 and num2<num3):
#     print("number is strictly increasing")
# else:
#     print("it is strictly decreasing")


# num=int(input("enter no:"))
# if(num%7==0 and not num%5==0 and abs(0<num<=100)):
#     print("number is multiple of 7 not of 5 and in range of 100")
# else:
#     print("not multiples")


# num=int(input("Enter no:"))
# a=0
# b=1
# for i in range (num):
#     print(a,end=" ")
#     a,b=b,a+b  
    
    
# num=int(input("enter a no:"))
# temp=num
# rev=0
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# print(rev)


#armstrong number
# num=int(input("enter no:"))
# temp=num
# sum=0
# b=len(str(num))
# while temp>0:
#     digit=(temp%10)**b
#     sum=sum+digit
#     temp=temp//10
# print(sum)
# if(num==sum):
#     print("it is armstrong number")
# else:
#     print("not")


# num=int(input("enter no:"))
# temp=num
# rev=0
# while temp>0:
#     rev=(rev*10) + (temp%10)
#     temp=temp//10
# print(rev)
# if(num==rev and rev%11!=0):
#     print("it is pallindrome and not divisible by 11")
# else:
#     print("unsatisfied condition")

# import math
# num=int(input("enter no to be checked:"))
# root=math.sqrt(num)
# if(num==root**2):
#     print("it is a sqare not a cube")
# else:
#     print("unsatisfied condition")

# num=int(input("enter no:"))
# if(num%3==0 or num%5==0 and not num%3==0 and num%5==0):
#     print("a number is divisible by either 3 or 5 but not both")
# else:
#     print("unsatisfied condition")


# num1=int(input("enter no:"))
# num2=int(input("enter no:"))
# num3=int(input("enter no:"))
# num4=int(input("enter no:"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("num1  is greater")
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("num2 is greater")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print("num3 is greater")
# else:
#     print("num4 is greater")


# year=int(input("enter no to be checked:"))
# if(year%4==0 and year%400==0 and year%1000!=0):
#     print("a year is leap year AND divisible by 400 but not by 1000")
# else:
#     print("not a leap year")
    
    
# num=int(input("enter no:"))
# temp=num
# rev=0
# while temp>0:
#     rev=rev*10 +(temp%10)
#     temp=temp//10
# if(rev==num):
#     print("num is a palindrome")
# else:
#     print("not palindrome")


# num=int(input("enter a no:"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#             print("prime")

# num=int(input("enter a no:"))
# rev=0
# temp=num
# while temp>0:
#     rev=rev*10+(temp%10)
#     temp=temp//10
# print(rev)



# num=int(input("enter a no:"))
# if num<=1:
#     is_prime=False
# else:
#     is_prime=True
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             is_prime=False
#             break
# orginal=num
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
    
# is_palindrome=(orginal==rev)
# if(is_prime and is_palindrome):
#     print("it is prime number and a palindrome")
# else:
#     print("not")


# n = int(input("Enter number: "))

# # Check Prime
# if n <= 1:
#     is_prime = False
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# # Check Palindrome
# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# is_palindrome = (original == reverse)

# # Final Result
# if is_prime and is_palindrome:
#     print("Number is both Prime and Palindrome")
# else:
#     print("Number is NOT both Prime and Palindrome")

# num=int(input("enter a no:"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")



# n=int(input("enter a no:"))
# if n<=1:
#     is_prime=False
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if(n%i==0):
#             is_prime=False
#             break
# original=n
# rev=0
# while (n>0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# is_palindrome=(original==rev)
# if(is_palindrome and is_prime):
#     print("no is both")
# else:
#     print("not")


# import math
# num=int(input("enter a no:"))
# root=math.sqrt(num)
# if(num==root**2):
#     print("it is a perfect square")
# else:
#     print("not the perfect square")
    
    
# num=int(input("enter a no:"))
# if(num%3==0 or num%5==0 and not (num%3==0 and num%5==0)):
#     print("number is divisible by either 3 or 5 but not by both")
# else:
#     print("unsatisfied condition")

# num1=int(input("enter a no :"))
# num2=int(input("enter a no :"))
# num3=int(input("enter a no :"))
# num4=int(input("enter a no :"))
# if(num1>num2 and num1>3 and num1>num4):
#     print("num1")
# if(num2>num1 and num2>num3 and num2>num4):
#     print("num2")
# if(num3>num2 and num3>num1 and num3>num4):
#     print("num3")
# else:
#     print("num4")


# year=int(input("enter a no:"))
# if(year%4==0 and year%400==0 and year%1000!=0):
#     print("satisfied")
# else:
#     print("unsatisfied")

# num=int(input("enter no:"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")

# num=int(input("enter a no:"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#             print("prime")


# n=int(input("enter a no:"))
# if n<=1:
#     print("not prime")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if(n%i==0):
#             print("not prime")
#             break
#     else:
#         print('prime')



# n=int(input("enter a no:"))
# if n<=1:
#     is_prime=False
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if(n%i==0):
#             is_prime=False
#             break
# original=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# is_palindrome=(rev==original)
# if(is_palindrome and is_prime):
#     print("no is both")
# else:
#     print("unsatisfied condition")






# n=int(input("enter a no:"))
# #now check prime first

# if n<=1:
#     is_prime=False
# else:
#     is_prime=True #condition given now we have to prove this
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0:
#             is_prime=False
#             break
# #checking palindrome
# org=n
# rev=0
# while n>0:
#     rev=rev*10+(n%10)
#     n=n//10
# is_palindrome=(org==rev)
# if(is_prime and is_palindrome):
#     print("condition satisfied")
# else:
#     print("unsatisfied condition")






# #harshad number (where sum of its digit divides it properly)
# n=int(input("enter a no:"))
# #we have to find sum of its digit
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10
# #now we have stored sum value 
# if(n%sum==0):
#     print("harshad no:")
# else:
#     print("not harshad no")






#automorphic no.(number's square ends with number)
# n=int(input("enter a no:"))
# sq=n**2
# while n>0:
#     digit=sq%10
#     break
# if(n==digit):
#     print("automorphic no")
# else:
#     print("not")
    




# n=int(input("enter no:"))
# sq=n**2
# while n>0:
#     digit=sq%10
#     break
# if(n==digit):
#     print("automorphic no")
# else:
#     print("not")



# n=int(input("enter no:"))
# if n<=1:
#     is_prime=False
# else:
#     is_prime=True
#     for i in range (2,int(n**2)+1):
#         if n%i==0:
#             is_prime=False
# org=n
# rev=0
# while n>0:
#     rev=rev*10+(n%10)
#     n=n//10
# is_pal=(rev==org)
# if(is_prime and is_pal):
#     print("no is both")
# else:
#     print("not both")




# n=int(input("enter no:"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# if(n%sum==0):
#     print("harshad no.")
# else:
#     print("not harshad no")
    
    
    
# n=int(input("enter no:"))
# sq=n**2
# while n>0:
#     digit=sq%10
#     break
# if(n==digit):
#     print("automorphic no")
# else:
#     print("not")




#perfect no (number's divisor's sum divides the number itself properly)
# n=int(input("enter no:"))
# sum=0
# for i in range (1,n):
#     if n%i==0:
#         sum=sum+i
# if(sum==n):
#     print("perfect no")
# else:
#     print("not")

    
 #fibonacci series    
# n=int(input("enter no:"))
# a=0  #these 2 a=0 b=1 are initial condition of a fibonacci series 
# b=1
# for i in range(n):
#     print(a," ")
#     a,b=b,a+b



