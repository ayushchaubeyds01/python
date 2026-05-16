# Check if the number is positive, negative, or zero
a=int(input("enter a number: "))

if a%2==0:
    print("even number")
elif a==0:
    print("zero")
else:
    print("odd number")
    
    
#elig1ibility to vote
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
    
    
#even or odd
num=int(input("enter a number: "))
if num%2==0:
    print("even number")
else:
    print("odd number")
    
    
    
    
#weeks 
days=int(input("enter number of days "))

match days:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6: 
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input")
        
        
        
        
        
#simple calculator
a=int(input("enter first number: "))
b=int(input("enter second number: "))
op=input("enter operator (+,-,*,/): ")
match op:
    case "+":
        print("sum:", a+b)
    case "-":
        print("subtraction:", a-b)
    case "*":
        print("multiplication:", a*b)
    case "/":
        print("division:", a/b)
    case _:
        print("invalid operator")
        
        
        
#loop to print numbers from 1 to 10
for i in range(1,11):
    print(i)
    
#multiplication table of a number
num=int(input("enter a number to print its multiplication table: "))
for i in range(1,11):
    print(num*i)
    
    #sum of first n natural numbers
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of first", n, "natural numbers is:", sum)




#star pattern
n=int(input("enter number of rows: "))
for i in range(1,n+1):
    print("* "*i)
    
    
    
#while loop to print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1

        
    #password checker
password="admin123"
user_input=input("enter your password: ")
while user_input!=password:
    print("incorrect password, try again")
    user_input=input("enter your password: ")
print("password correct, access granted")



#for loop with break statement
for i in range(1,11):
    if i==7:
        break
    print(i)
    
    
    #for loop with continue statement
for i in range(1,11):
    if i==5:
        continue
    print(i)
    
    #for loop with pass statement
    
    
for i in range(1,11):
    if i%2==0:
        pass
    print(i)