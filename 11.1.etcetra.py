### sets

# 
# students=[
#     {"name":"hermione","house":"gryffindor"},
#     {"name":"harry","house":"gryffindor"},
#     {"name":"ron","house":"slytherine"},
#     {"name":"draco","house":"ravenclaw"},
    
# ]
# now sort it  using lists
# houses=[]
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
# for house in sorted(houses):
#     print(house)
    
### but we can do it using a set 

# houses=set()
# for student in students:
#     houses.add(student["house"])
# for house in sorted(houses):
#     print(house)






##### global - it is a keyword used to define a variable that can be used in whole program / function

# balance=0
# def main():
#     print(balance)
#     deposit(100)
#     withdraw(50)
#     print(balance)
# def deposit(n):
#     global balance
#     balance+=n
# def withdraw(n):
#     global balance
#     balance-=n

# if __name__=="__main__":
#     main()



## we can solve this problem using oop too

# class Account:
#     def __init__(self):
#         self._balance=0
#     @property
#     def balance(self):
#         return self._balance
#     def deposit(self,n):
#         self._balance+=n
#     def withdraw(self,n):
#         self._balance-=n
# def main():
#     account=Account()
#     print(account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print(account.balance)
# if __name__=="__main__":
#     main()




# ### type hints
# def meow(n : int) -> str:      ## here : int gives type hint of users input  and -> str gives type hint of return type
#     return ("meow\n")*n
# number : int = int(input("n:"))
# meows : str=meow(number)
# print(meow(number))







## docstring   used to describe what is the use of that function variable or anything inside that program

# def meow(n : int) -> str:
#     """
#     moew n times
#     n: no of times to meow
#     type n: int
#     return : a str of meow
#     rtype : str
#     raise TypeError if n is not int 

# # it is a docstring that tells the intent of program
#     """
#     return ("meow\n")*n
# number : int = int(input("n:"))
# meows : str=meow(number)
# print(meow(number))
# # we can print the docstring by
# print(meow.__doc__)










## argparse - library used to give cli commands 
# without argparse
# import sys
# if len(sys.argv)==1:
#     print("meow")
# elif(len(sys.argv))==3 and sys.argv[2]==" -n":
#     n=int(sys.argv[2])
#     for _ in range (n):
#         print("meow")
# else:
#     print("usage: meows.py")
        
# it is harder to check and pass cli values so we use argparse 





# using argparse



# import argparse




# parser=argparse.ArgumentParser(description="meow like a cat")    # ArguementParser reads command line arguements
# parser.add_argument("-n",default=1,help="no of times to meow",type=int)    # parser.add_arguement creates command line arguement
# args=parser.parse_args()     #reads what user has typed in terminal
# for _ in range(args.n):     #args.n saves the value of user's input
#     print("meow")











## unpacking 

# def total(galleons ,  sickles , knuts):
#     return (galleons *17 + sickles)*29+knuts
# coins=[100,50,25]

# print(total(coins[0],coins[1],coins[2]))  # it's just a manual way if there will be more values it will be tough 
# print(total(*coins))    # this asterisk sign * before list unpacks the value left to right


# but what happens we have a dictionary instead of a list
# coins={"galleons":100,"sickles":50,"knuts":25}

# print(total(coins["galleons"],coins["sickles"],coins["knuts"]))  # this is also kind of manual and tough when there are more values 
# print(total(**coins))    # this asterisk sign ** before dictionary unpacks the value left to right












############   *args and **kwargs


