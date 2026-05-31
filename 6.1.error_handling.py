# try:
#     x=int(input("Enter x:"))
#     print(x)
# except ValueError:
#     print("it is not an integer")


# #name error
# try:
#     x=int(input("Enter x:"))
# except ValueError:
#     print("it is not an integer")
# else:
#     print(f"x is {x}") 



# while True:
#     try:
#         x=int(input("enter x:"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

#or in shorter version 


# while True:
#     try:
#         x=int(input("Entre x:"))
#         break
#     except:
#         print("x is not an integer")
# print(f"x is {x}")



# # now we can invent out own function
# def main():
#     x=get_int()
#     print(f"x is  {x}")
# def get_int():
#     while True:
#         try:
#             x=int(input("Enter x:"))
#             break
#         except:
#             print("x is not an integer")
#     return x
# main()






# #now when we don't want  to get an output for an exception we use pass
# def main():
#     x=get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             return int(input("enter x:"))
#         except:
#             pass
# main()



# #now we can pass arguements to the function

# def main():
#     x=get_int("what's x?")
#     print(f"x is {x}")
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except:
#             pass
# main()