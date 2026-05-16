# a='1'
# # if a==18:
# #     print("you are eligible to vote")
# # elif a>18:
# #     print("you are  eligible to vote and you can drive")
# # else:
# #     print("you are not eligible to vote")

# try:
#     int(a)

# except:
#     a=4
    
# print(a)

# try is blowed up when that piece of code is wrong and except block of code is executed and  vice versa

# a="ayush"
# a=3
# try:
#     print("hello",a)
#     b=int(a)
#     print(b)
# except:
#     print("ayush chaubey")
    

# a=(input("enter no:"))
# try:
#     print(a)
#     b=int(a)
#     print(b)
# except:
#     print("invalid")
# if(a>0):
#     print("noice")
# else:
#     print("not nice work")


# a=int(input("enter no:"))
# b=int(input("enter no:"))
# if(a>b):
#     print("a is greater")
# elif(a<b):
#     print("b is geater")
# else:
#     print("both are equal")

# score=int(input("enter no :"))
# if(90<score and score<=100):
#     print("Grade A")
# elif(80<score and score<=90):
#     print("Grade B")
# elif(70<score and score<=80):
#     print("Grade C")
# else:
#     print("Grade F")

# score=int(input("enter no :"))
# if(score>=90):
#     print("A")
# elif(score>=80):
#     print("B")
# elif(score>=70):
#     print("C")
# else:
#     print("F")

# def main():
#     i=int(input("enter no:"))
#     if(is_even(i)):
#         print("Even")
#     else:
#         print("odd")
# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# main()

def main():
    a=int(input("enter no:"))
    if is_even(a):
        print("Even")
    else:
        print("odd")
def is_even(n):
    # return True if n%2==0 else False
    # if(n%2==0):
    #     return True
    # else:
    #     return False 
    return n%2==0
main()
