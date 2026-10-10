# try:
#     x=int(input("enter x:"))
# except ValueError:
#     print(" x is nt an integer")
# else:
#     print(f"x is {x}")




# division 



# try:
#     x=int(input("enter n:"))
#     y=int(input("enter n:"))
#     result=x/y
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter integer")
# else:
#     print(result)



# # input conversion
# def main():
#     x=conversion()
# def conversion():
#     try:
#         a=int(input("enter n:"))
#     except ValueError:
#         print("try something else")
#     else:
#         print(f"a is {a}")
# main()



# # square of a number
# def main():
#     x=square()
# def square():
#     try:
#         a=int(input("enter n:"))
#         result=a*a
#     except ValueError:
#         print("a is not integer")
#     else:
#         print(result)
# main()






# get Index
# def main():
#     b=get_index()
# def get_index():
#     num=[1,2,3,4,5]
#     try:
#         x=int(input("enter index:"))
#         result=num[x]
#     except IndexError:
#         print("index out of range")
#     else:
#         print(result)
# main()





# # calculator
# def main():
#     calculator()
# def calculator():
#     try:
#         x=int(input("enter x:"))
#         y=int(input("enter y:"))
#         op=input("enter :")
#         add=x+y
#         sub=x-y
#         mul=x*y
#     except ValueError:
#         print("try integer")
        
#     else:
#         if "+" in op:
#                     print(add)
#         elif "-" in op:
#                     print(sub)
#         elif "*" in op:
#                     print(mul)
#         elif "/" in op:
#             try :
#                 div=x/y
#             except ZeroDivisionError:
#                     print("zero se divide nhi hoga")
#             else:
#                     print(div)
#         else:
#                     print("choose valid oprator")
# main()





# # dictonary lookup
# def main():

#     get_marks()
# def get_marks():
#     students = {
#             "Rahul": 85,
#             "Priya": 92,
#             "Amit": 78
#         }
    
#     try:
#         name=input("enter name:")
#         result=(students[name])
#     except KeyError:
#         print("name not in dct")
#     else:
#         print(result)
# main()







# # age validation
# def main():
#     get_age()
# def get_age():
#     try:
#         age=int(input("enter age:"))
#     except ValueError:
#         print("age is not valid")
#     else:
#         print(f"age is {age}")
# main()




# # multiple exceptions
# def main():
#     check_div()
# def check_div():
#     try:
#         n1=int(input("enter n1:"))
#         n2=int(input("enter n2:"))
#         result=n1/n2
#     except ValueError:
#         print("try something else")
#     except ZeroDivisionError:
#         print("zero nahinnnn")
#     else:
#         print(result)
# main()







# # calculate percentage
# def main():
#     get_per()
# def get_per():
#     try:
#         total_marks=int(input("enter total marks:"))
#         obt_marks=int(input("enter obt marks:"))
#         result=(obt_marks/total_marks)*100
#     except ValueError:
#         print("enter integer")
#     except ZeroDivisionError:
#         print("bokachand")
#     else:
#         print(result)
# main()





# check positive negative and zero
# def main():
#     check_num()
# def check_num():
#     try:
#         n=int(input("enter n:"))
#     except ValueError:
#         print("try integer")
#     else:
#         if n>0:
#             print("positive")
#         elif n<0:
#             print("negative")
#         else:
#             print("zero")
# main()









# # file handle
# def main():
#     check_file()
# def check_file():
#     try:
#         with open ("data.txt","r") as file:
#             content=file.read()
            
#     except FileNotFoundError:
#         print("try with diff file")
#     else:
#         print(content)
# main()





# # nested questions
# def main():
#     validate()
# def validate():
#     try:
#         n=int(input("enter n:"))
#         n2=int(input("enter n2:"))
        
#         try:
#             result=n/n2
#         except ZeroDivisionError:
#             print("zero se nahin hoga")
#         else:
#             print(result)
#     except ValueError:
#         print("try integers")
#     else:
#         print("Both inputs are valid integers")
#     finally:
#         print("execution successful")
# main()







# # file handeling
# def main():
#     check()
# def check():
#     try:
#         with open("data.txt","r") as file:
#             content=file.read()
#     except FileNotFoundError:
#         print("try diff file name")
#     else:
#         print(content)
#     finally:
#         print("File operation completed")
# main()





# # age validation
# def main():
#     check()
# def check():
#     try:
#         age=int(input("enter age"))
#         if age<0:
#             raise ValueError  ("age cannot be negative")
#     except ValueError as e:
#         print("enter integer",e)
#     else:
#         print(age)
#     finally:
#         print("validation completed")
# main()

