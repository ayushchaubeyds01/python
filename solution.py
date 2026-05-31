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



# print("Ayush kumar chaubey")
# name=input("enter name:")
# print(name)

# a=1;b=2
# print(a+b)
# print(a*b)


# a=3;b=4;c=5
# print(a+b+c)/3

# a=5
# b=3
# c=a
# a=b
# b=c
# print(a)
# print(b)


# a=4
# b=2
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)


# c=int(input("enter c:"))
# f=((9/5)*c)+32
# print(f)


# f=float(input("enter f:"))
# c=(f-32)*(5/9)
# print(c)


# km=float(input("enter km:"))
# m=km*1000
# print(m)


# min=int(input("enter no of minutes:"))
# hr=min*60
# print(hr)


# length=float(input('enter length:'))
# breadth=float(input('enter breadth:'))
# print(length*breadth)


# import math
# r=float(input("enter radius:"))
# print(3.14*r*r)


# p=int(input("enter p:"))
# r=int(input("enter r:"))
# t=int(input("enter t:"))
# si=(p*r*t)/100
# print(si)


# p=int(input("enter p:"))
# r=int(input("enter r:"))
# n=int(input("enter n:"))
# a=p*((1+(r/100))**(n))
# ci=a-p
# print(ci)



# num=int(input("enter no:"))
# print(num**2)
# print(num**3)


# char=input("enter a char:")
# print(ord(char))


# a=45
# b=a%10
# print(b)


# p=45
# m=67
# b=67
# c=59
# e=78
# print(p+c+b+m+e)/5


# days=int(input("enter no of days:"))
# year=days/365
# month=days/30
# print(month)
# print(year)

# a=45
# b=a//10
# print(b)

# unit_per_day=float(input("Enter amount of unit"))
# no_of_day_to_be_counted=int(input("Enter no of days:"))
# print("bill=",unit_per_day*no_of_day_to_be_counted)





# num=int(input("enter no:"))
# if num%2==0:
#     print("Even")
# else:
#     print("odd")
    
    
    
    
    
    
    
    
# num=int(input("enter no:"))
# if num<0 :
#     print("positive")
# elif(num==0):
#     print("is zero")
# else:
#     print("negative")






# num1=int(input("enter no:"))
# num2=int(input("enter no:"))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")






# num1=int(input("enter no:"))
# num2=int(input("enter no:"))
# num3=int(input("enter no:"))
# if num1>num2 and num1>num3:
#     print("num1 is greater")
# elif(num2>num1 and num2>num3):
#     print("num2 is greater")
# else:
#     print("num3 is greater")








# num1=int(input("enter no:"))
# num2=int(input("enter no:"))
# num3=int(input("enter no:"))
# if num1<num2 and num1<num3:
#     print("num1 is smaller")
# elif(num2<num1 and num2<num3):
#     print("num2 is smaller")
# else:
#     print("num3 is smaller")






# num=int(input("enter no:"))
# if num%5==0:
#     print("number is divisible by 5")
# else:
#     print("not divisible")







# num=int(input("enter no:"))
# if num%5==0 and num%11==0:
#     print("number is divisible by 5 and 11 both")
# else:
#     print("not divisible")







# num=int(input("enter no:"))
# if num%3==0 and num%7==0:
#     print("number is divisible by 3 and 7 both")
# else:
#     print("not divisible")







# year=int(input("enter year to be checked:"))
# if year %4==0:
#     print("year is leap year")
# else:
#     print("not a leap year")
    







# vowel='a','e','i','o','u'
# char=input("enter char to be checked")
# if char in vowel:
#     print("char is a vowel")
# else:
#     print("char is consonent")








# char=(input("enter char:"))
# if 48< ord(char)<=57:
#     print("it is a digit")
# elif(65<ord(char)<=90 or 97<ord(char)<=122):
#     print("it is alphabet")
# elif(33<ord(char)<=64):
#     print("it is special charecter")
# else:
#     print("invalid input")







# char=(input("enter char:"))
# if (65<ord(char)<=90):
#     print("it is uppercase")
# elif(97<ord(char)<=122):
#     print("it is a lowercase")
# else:
#     print("invalid input")






# marks=int(input("enter marks:"))
# if marks>=90:
#     print("A")
# elif marks>=90:
#     print("B")
# elif marks>=90:
#     print("C")
# elif marks>=90:
#     print("D")
# elif marks>=90:
#     print("F")
# else:
#     print("invalid marks")







# price=5000
# if price<4000 :
#     print("profit")
# else:
#     print("loss")







# side1=int(input("enter side1:"))
# side2=int(input("enter side2:"))
# side3=int(input("enter side3:"))
# if(side1+side2>side3):
#     print("it is a triangle")
# else:
#     print("it is not")
    







# # side1=int(input("enter side1:"))
# # side2=int(input("enter side2:"))
# # side3=int(input("enter side3:"))
# if (side1==side2==side3):
#     print("it is equilateral triangle")
# elif(side1==side2!=side3):
#     print("it is isoscales triangle")
# else:
#     print("it is scalane triangle")







# b=int(input("enter b:"))
# a=int(input("enter a:"))
# c=int(input("enter c:"))
# d=(b**2)-4*a*c
# if(d>0):
#     print("roots are real and diffrent")
# elif(d==0):
#     print("roots are real and unique ")
# elif(d<0):
#     print("imaginary roots")





# age=int(input("enter age:"))
# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible")






#suppose consumer consumes 250 units in a month
# slab_unit=int(input("enter slab unit:"))
# if(0<slab_unit<=100):
#     print("per unit rate=4.50",",","cost=",slab_unit*4.50)
# elif(100<slab_unit<=200):
#     print("per unit rate=6.00",",","cost=",slab_unit*6.00)
# elif(200<slab_unit<=250):
#     print("per unit rate=7.50",",","cost=",slab_unit*7.50)
# else:
#     print("invalid entry")





#suppose you go to atm  and bank balance is 1 lakh
# balance=100000
# print("insert the card")
# pin=int(input("enter pin:"))
# print("select withdrawl")
# withdrawl_amount=int(input("enter withdrawl amount:"))
# if(withdrawl_amount<=100000):
#     print("withdraw money")
# else:
#     print("insufficient balance")




# password=191984
# enter_pass=int(input("enter pin:"))
# print(enter_pass)
# if(enter_pass==password):
#     print("password unlocked")
# else:
#     print("password is wrong")




# salary=int(input("enter salary:"))
# if(salary<=10000):
#     print("bonus=1500")
# elif(10000<salary<=50000):
#     print("bonus=5000")
# elif(50000<salary<=100000):
#     print("bonus=10000")
# elif(100000<salary<=500000):
#     print("bonus=50000")
# else:
#     print("1 piece of cup")
    
    
    

 
# age=int(input("enter age:"))
# if(18<age<=65):
#     print("eligible for insurance")
# else:
#     print("not eligible")


# num=float("enter no:")
# if(num==abs(num)):
#     print("it is absolute number")
# else:
#     print("not a absolute no")



# n=int(input("enter no:"))
# m=int(input("enter no:"))
# if(n%m==0):
#     print("n is multiple of all entered m")
# else:
#     print("not a multiple")


# print("1.+ ,2.-,3.*,4./")
# choice=input("enter oprator")
# a=int(input("enter no1:"))
# b=int(input("enter no2:"))
# if(choice == "+"):
#     print(a+b)
# elif(choice == "-"):
#     print(a-b)
# elif(choice == "*"):
#     print(a*b)
# elif(choice == "/"):
#     print(a/b)
# else:
#     print("invalid oprator")4


# month=input("enter month:")
# if  month=="january" and month=="feb" and month=="march":
#     print("winter")
# elif(month=="april"and month=="may" and month=="june"):
#     print("summer")
# elif(month=="july"and month=="aug" and month=="sep"):
#     print("monsoon")
# elif(month=="oct"and month=="nov" and month=="dec"):
#     print("winter")
# else:
#     print("invalid input")
    
    
    
# n=int(input("enter no of  day:"))
# if(n==1):
#     print("sunday")
# elif(n==2):
#     print("monday")
# elif(n==2):
#     print("tue")
# elif(n==2):
#     print("wed")
# elif(n==2):
#     print("thru")
# elif(n==2):
#     print("fri")
# elif(n==2):
#     print("sat")
# else:
#     print("invalid input")



# product=input("enter product")
# if(product =="gold"):
#     print("shipping charge=1000")
# else:
#     print("shipping charge= 500")





# product=input("enter product:")
# product_price=input("enter product:")

# if(product_price<=1000):
#     print("discount= 15%")
# if(1000<product_price<=10000):
#     print("discount= 25%")
# if(10000<product_price<=20000):
#     print("discount= 30%")
# if(20000<product_price<=50000):
#     print("discount= 45%")
# else:
#     print("discount= 5%")




# salary=int(input("enter salary:"))
# if salary<=800000:
#     print("no income tax")
# elif(800000<salary<=2000000):
#     print("12% income tax")
# elif(2000000<salary<=4000000):
#     print("20% income tax")
# elif(4000000<salary<=10000000):
#     print("25% income tax")
# else:
#     print("invalid input")



# num=int(input("enter number:"))
# b=str(num)
# c=b[::-1]
# if c==b:
#     print("it is palindrome")
# else:
#     print("not a palindrome")



# import math
# num=int(input("enter number"))
# b=math.isqrt(num)
# if(num==b**2):
#     print("it is perfect square")
# else:
#     print("it is not")



#suppose range is of 10 to 20
# num=int(input("enter number"))
# if(10<num<=20):
#     print("number is in range of 10  to 20")
# else:
#     print("not in range")




# year=int(input("enter year:"))
# if(year%100==0):
#     print("it is a century year")
# else:
#     print("it is not")









































#loops




# for i in range (1,101):
#     print(i)

# for i in range (100,1,-1):
#     print(i)


# for i in range (100):
#     if i%2==0:
#         print(i)


# for i in range(100):
#     if i%2!=0:
#         print(i)




#sum of 1st n numbers
# n=int(input("enter no:"))
# sum=0
# for i in range(n+1):
#     sum+=i
# print(sum)



# #product of 1st n numbers
# n=int(input("enter n:"))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(product)



# #multiplication table
# limit=int(input("enter limit:"))
# n=int(input("enter limit:"))
# for i in  range(1,limit+1):
#     print(i*n)



# n=int(input("enter n:"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)




# n=int(input("enter n:"))
# p=int(input("enter raised power:"))
# for i in range (1,n+1):
#     power=pow(n,p)
# print(power)



# #fibbonaci series
# n=int(input("enter n:"))
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     a,b=b,a+b




# #count digits
# n=int(input("enter n:"))
# b=str(n)
# count=0
# for i in range(1,len(b)+1):
#     digit=n//10
#     count+=1
# print(count)




# #sum of digit
# n=int(input("enter n:"))
# sum=0
# for i in range (1,n+1):
#     digit=n% 10               #% is used to get last digit       
#     sum+=digit
#     n=n//10                   // is used to remove the last digit
# print(sum)








# #reverse a no
# n=int(input("enter n:"))
# rev=0
# b=str(n)
# for i in range (1,len(b)+1) :
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)



# #palindrome no
# n=int(input("enter n:"))
# b=len(str(n))
# org=n
# rev=0
# for i in range (1,(b)+1):
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if (org==rev):
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")





# #armstrong number = no has n number of digit then sum of each digit with total no of  digit raised power equals to number itself
# n=int(input("Enter n:"))
# b=len(str(n))
# org=n
# sum=0
# for i in range(1,b+1):
#     digit=n%10
#     sum+=digit**b
#     n//=10
# print(sum)
# if(sum==org):
#     print("it is armstrong number")
# else:
#     print("it is not armstrong number")





##prime number
# n=int(input("Enter no."))
# if n<=1:
#     is_prime=False
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("it is prime")



# # #strong number  =no whose sum of factorial is no itslf
# n=int(input("enter n:"))
# sum=0
# temp=n
# b=len(str(n))
# for i in range (1,b+1):
#     digit=temp%10
#     fact=1
#     for j in range (1,digit+1):
#         fact*=j
#     sum+=fact
#     temp//=10
# if sum==n:
#     print("strong number")
# else:
#     print("it is not")





# #perfect number  = no whosse divisor sum is number itself
# n=int(input("enter n:"))
# sum=0
# #find divisors first
# for i in range (1,n):
#     if n%i==0:
#         sum+=i #add all divisor to sum
# print(sum)
# if sum==n:
#     print("it is a perfect no")
# else:
#     print("it is not a strong number")



# #automorphic number =  no whose square ends wtih number itself
# n=int(input("enter n:"))
# power=n**2
# b=len(str(power))
# for i in range (b):
#     digit=power%10
# if digit==n:
#         print("it is ")
# else:
#         print("it is not")



# #harshada numbers
# n=int(input("enter n:"))
# sum=0
# temp=n
# for i in range(1,n+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if (n%sum==0):
#     print("harshad number")
# else:
#     print("not a harshad number")




# #neon number
# n=int(input("enter n:"))
# sq=n**2
# temp=sq
# b=len(str(sq))
# sum=0
# for i in range (1,b+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if (sum==n):
#     print("it is neon number")
# else:
#     print("it is not a neon number")




# #prime number
# n=int(input("enter n:"))
# if n<=1:
#     is_prime=False
# else:
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")



# #prime number from 1 to 100
# for num in range (1,101):
#     if num<=1:
#         is_prime=False
#     else:
#         for i in range (2,int(num**0.5)+1):
#             if num%i==0:
#                 break
#         else:
#             print(num)


# n=int(input("enter n:"))
# is_prime=True
# for i in range(1,n+1):
#     if i<=1:
#         is_prime=False
#     else:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#         else:
#             print(i,"prime")


# #twin prime numbers
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# if n1<=1:
#     is_prime=False
# else:
#     for i in range(2,int(n1**0.5)+1) and (2,int(n2**0.5)+1):
#         if n1%i==0 and n2%i:
#             break
#     else:
#         if n1-n2==2:
#             print("it is twin prime")
#         else:
#             print("not twin prime")




# #prime factors
# n=int(input("enter n:"))
# for i in range(2,n):
#     if n%i==0:
#         print(i)
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 print("not a prime factor")
#                 break
#             else:
#                 print("factors is prime")




# #lcm
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(max(n1,n2),n1*n2+1):  #as lcm of 2  num is always less than their multiplication
#     if i%n1==0 and i%n2==0:   #which lowest value divisible by both numbers
#         print(i)
#         break
    
    
    
# #hcf
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(min(n1,n2),0,-1): #min is used because hcf of 2 num cannot be greater than smaller number
#     if n1%i==0 and n2%i==0:  #factors which are common to divide both numbers
#         print(i)
#         break



# #nth prime

# n=int(input("enter n:"))
# for i  in range (1,n+1):
#     if n<=1:
#         is_prime=False
#     else: 
#             if n%i==0:
#                 print("not prime")
#                 break
#             else:
#                 print(n,"prime")
            
            
# for i in range(1,101):
#     print(i)


# for i in range(100,0,-1):
#     print(i)


# for i in range(1,101):
#     if i%2==0:
#         print(i)


# for i in range(1,101):
#     if i%2!=0:
#         print(i)


# n=int(input("Enter n:"))
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print(sum)



# n=int(input("Enter n:"))
# pro=1
# for i in range (1,n+1):
#     pro*=i
# print(pro)



# limit=int(input("enter limit:"))
# n=int(input("enter n:"))
# for i in range(1,limit+1):
#     print(i*n)



# n=int(input("enter n:"))
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print(fac)


# n=int(input("enter n:"))
# p=int(input("enter p:"))
# for i in range(1,n+1):
#     print(pow(n,p))
#     break


# n=int(input("enter n:"))
# a=0
# b=1
# for i in range (1,n+1):
#     print(a)
#     a,b=b,a+b


# n=int(input("enter n:"))
# b=len(str(n))
# count=0
# for i in range(1,b+1):
#     n//=10
#     count+=1
# print(count)


# n=int(input("enter n:"))
# sum=0
# temp=n
# for i in range(1,n+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# print(sum)


# n=int(input("enter n:"))
# rev=0
# b=len(str(n))
# for i in range(1,b+1):
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)



# n=int(input("enter n:"))
# rev=0
# b=len(str(n))
# org=n
# for i in range(1,b+1):
#     digit=org%10
#     rev=rev*10+digit
#     org//=10
# if(n==rev):
#     print("it is a palindrome")
# else:
#     print("it is not")


# n=int(input("enter n:"))
# b=len(str(n))
# org=n
# sum=0
# for i in range(1,b+1):
#     digit=org%10
#     sum+=digit**b
#     org//=10
# if sum==n:
#     print("armstrong number")
# else:
#     print("it is not")



# n=int(input("enter n:"))
# b=len(str(n))
# sum=0
# org=n
# for i in range(1,b+1):
#     digit=org%10
#     fac=1
#     for j in range(1,digit+1):
#         fac=fac*j
#     sum+=fac
#     org//=10
# if (sum==n):
#     print("strong num")
# else:
#     print("it is not")



# n=int(input("enter n:"))
# org=n
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("it is a perfect number")
# else:
#     print("it is not")




# n=int(input("enter n:"))
# sq=n**2
# temp=sq
# for i in range(1,sq+1):
#     digit=temp%10
#     break
# if digit==n:
#     print("automorphic number")
# else:
#     print("not")



# n=int(input("enter n:"))
# temp=n
# sum=0
# for i in range(1,n+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if n%sum==0:
#     print("harshad number")
# else:
#     print("not")


# n=int(input("enter n:"))
# sq=n**2
# sum=0
# temp=sq
# b=len(str(sq))
# for i in range(1,b+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if sum == n:
#     print("neon number")
# else:
#     print("not")

# n=int(input("enter n:"))
# if n<=1:
#     is_prime=False
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime no")



# for i in range (1,101):
#     if i<=1:
#         is_prime=False
#     else:
#         is_prime=True
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#         else:
#             print(i,"prime")


# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# if n1<=1 and n2<=1:
#     is_prime=False
# else:
#     for i in range (2,int(n1**0.5)+1) and (2,int(n2**0.5)+1):
#         if n1%i==0 and n2%i==0:
#             is_prime=False
#             break
#     else:
#         if n1-n2==2:
#             print("twin prime")
#         else:
#             print("not")



# n=int(input("enter n:"))
# for i in range(2,n):
#     if n%i==0:
#         print(i)
#         if i<=1:
#             is_prime=False
#         else:
#             for j in range (2,int(i**0.5)):
#                 if i%j==0:
#                     print("not a prime factor")
                    
#             else:
#                 print("prime factor")

# n=int(input("enter n:"))
# for i in range(2,n):
#     if n%i==0:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 print(i,"not a prime factor")
#                 break
#         else:
#             print(i,"prime factors")



# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(min(n1,n2),0,-1):
#     if n1%i==0 and n2%i==0:
#         print(i)
#         break



# #lcm
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(max(n1,n2),n1*n2+1):
#     if i%n1==0 and i%n2==0:
#         print(i)
#         break



# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if i<=1:
#         is_prime=False
#     else:
#         for j in range (2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#         else:
#             print(i,"prime")


# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if i<=1:
#         is_prime=False
#     else:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_prime=False
#                 break
#         else:
#             print(i,"prime")



# #co prime
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(min(n1,n2),0,-1):
#     if n1%i==0 and n2%i==0:
#         if i==1:
#             print("co prime")
#         else:
#             print("not")
#         break



# #sum of even digits
# n=int(input("enter n:"))
# b=len(str(n))
# sum=0
# for i in range(1,b+1):
#     digit=n%10
#     if digit%2==0:
#         sum+=digit
#     n//=10
# print(sum)



# #product of odd digit
# n=int(input("enter n:"))
# b=len(str(n))
# product=1
# for i in range(1,b+1):
#     digit=n%10
#     if digit%2!=0:
#         product*=digit
#     n//=10
# print(product)



# #largest digit in a number
# n=int(input("enter n:"))
# b=len(str(n))
# largest=0
# for i in range(1,b+1):
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     n//=10
# print(largest)



# #smallest digit in a number
# n=int(input("enter n:"))
# b=len(str(n))
# smallest=n%10
# for i in range(1,b+1):
#     digit=n%10
#     if digit<smallest:
#         smallest=digit
#     n//=10
# print(smallest)



# n=int(input("enter n:"))
# b=len(str(n))
# largest=0
# for i in range (1,b+1):
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     n//=10
# print(largest)



# n=int(input("Enter n:"))
# b=len(str(n))
# smallest=n%10
# for i in range(1,b+1):
#     digit=n%10
#     if digit<smallest:
#         smallest=digit
#     n//=10
# print(smallest)


# #frequency of a number
# n=int(input("Enter n:"))
# b=len(str(n))
# choice=int(input("enter choice:"))
# freq=0
# for i in range(1,b+1):
#     digit=n%10
#     if choice==digit:
#         freq+=1
#     n//=10
# print(freq)



# #binary to decimal
# n=int(input("Enter n:"))
# b=len(str(n))
# sum=0
# power=0
# for i in range(1,b+1):
#     digit=n%10
#     binary=digit*(2**power)
#     sum+=binary
#     n//=10
#     power+=1
# print(sum)



# #decimal to binary
# n=int(input("enter num:"))
# bin=""
# while n>0:
#     digit=n%2
#     bin=str(digit)+bin
#     n//=2
# print(bin)



# #decimal to octal
# n=int(input("enter n:"))
# octal=""
# while n>0:
#     digit=n%8
#     octal=str(digit)+octal
#     n//=8
# print(octal)


# #decimal to hexadecimal
# n=int(input("enter n:"))

# hexa=""
# while n>0:
#     digit=n%16
#     if digit<10:
#         hexa=str(digit)+hexa   
#     else:
#         hexa=chr(digit+55)+hexa
#     n//=16
# print(hexa)




# #spy numbers === whose sum of digit = product of digits
# n=int(input("enter n:"))
# b=len (str(n))
# sum=0
# product=1
# for i in range(1,b+1):
#     digit=n%10
#     sum+=digit
#     product*=digit
#     n//=10
# if sum==product:
#     print("spy numbers")
# else:
#     print("not")


######series problems
#sum of squares
n=int(input("enter n:"))
sum=0
for num in range(1,n+1):
    digit=(num)%10
    sum+=digit
    num//=10
print(sum)