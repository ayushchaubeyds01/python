# for i in range(1,10000):
#     print(i)
# a=int(input("enter a number to print its multiplication table: "))
# for i in range(1,11):
#     print(a*i)


# for j in [0,1,2]:
#     print("Meowww")  
    #  or
    
# for j in range(3):
#     print("mew")

#or 

# for _ in range(3):
#     print("mew")



#or 

# print("mew\n"*3,end="")



# s=str(input("enter no :"))
# for i in range (5,0,-1):
#     print(s*i)
    
    
    
# for char in "leopard":
#     print(char)



# for anime in ['one piece ','naruo','boruto']:
#     print(anime)

# for key in {'A101': 'RAJESH'}:
    # print(key)
    
# lis=['dessert','fruit']
# for i in enumerate(lis):
#     print(i)



# n=int(input("enter a no:"))
# if n<1:
#     print("not prime ")
# else:
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#           print("prime")





# n=int(input("enter no:"))
# for i in range (1,n+1):
#     print("*"*i)




# for i in range (65,91):
#     print(chr(i),end=" ")
# print()   #prints the new  line
# for j in range(122,98,-1):
    
#     print(chr(j),end=" ")



# for count in range (1,11):
#     print(count)


# for index in range (20,10,-3):
#     print(index)


# for odd in range(1,26):
#     if(odd%2!=0):
#         print(odd)

# lst=['desert','dessert','to','too','lose','loose']
# s='mumbai'
# for i in range (len(lst)):
#     if i>3:
#         break
#     else:
#         print(i,lst[i],s[i])




# # wap to count number of alphabet and digit in a string nagpur-440010
# s=input("enter char:")
# digit=0
# alpha=0
# for ch in (s):
#     if ch.isalpha():
#         alpha+=1
#     elif(ch.isdigit()):
#         digit+=1
# print(alpha)
# print(digit)






# n=int(input("enter no:"))
# b=str(n)
# rev=0
# temp=n
# for i in range (1,len(b)+1):
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# print(rev)

# if(rev==n):
#     print("equal")
# else:
#     print("not equal")


# n=int(input("enter no:"))
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# # print(fact)


# num = int(input("Enter a number: "))

# # Convert number to string to count digits
# n = len(str(num))

# result = 0

# # Using for loop
# for digit in str(num):
#     result += int(digit) ** n
# print(result)
# # Check Armstrong
# if result == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")
    
    
    
    
    
    
# #arnstrong no
    
# n=int(input("enter a no:"))
# b=len(str(n))
# sum=0
# for i in (str(n)):
#     sum+=int(i)**b
# print(sum)



#prime no 

# n=int(input("enter no between 1 and 300:"))
# if n<=1:
#     print("not prime")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if(n%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")



#multiplication table
# n=int(input("enter no:"))
# limit=int(input("enter no:"))
# for i in range(1,limit+1):
#     print(n,"*",i,"=",n*i)


for i in range (1,5):
    print(i)