# i=1
# while i<=10:
#     print(i)
#     i+=1


# i=3
# while i!=0:
#     print("meowwwwwwwwwwwwwwwwwww")
#     i=i-1

    
    # flowchart of loop 
    
    #start
    #  |
    # i=3
    #  |
    # i!=0
    #  |
    # if false ----- stop 
    # if not false ---------print(meow)
    #                           | 
    #                     i=i-1 (continuously updates i with each itration )
    #                         #now after updating i move to check value of i 
    
    
    
# i=0
# while i <=3:
#     print("mew")
#     i+=1


# i=int(input("enter a no:"))
# while i<1:
#     print("meow")
#     break
# else:
#     print("hello cat")    




# #square of a no
# n=7
# while  n!=5:
#     num=int(input("enter no:"))
#     print(num,num*num)




# count=0
# while count<10:
#     print(count)
#     count+=1




# #loop over a string 
# s="ayush"
# i=int(input("enter no"))
# while i<len(s):
#     print("hello ayush\n"*len(s))
#     break




# n=int(input("enter no:"))
# i=2
# while i <=n-1:
#     if n%i==0:
#         print("not prime")
#         break
#     i+=1
# else:
#     print("prime")
    
    
#############################questions

#wap to reccieve 3 set of values p n and r and calculate simple intrest of each set 

#solution 

# i=1
# while i<=3:
#     p=float(input("enter no:"))
#     r=float(input("enter no:"))
#     t=float(input("enter no:"))
#     si=(p*r*t)/100
#     print(si)
#     i+=1


# i=1 #itration input
# while i<=3:   #as we need 3 sets loop will terminate after third value
#         p=float(input("enter no:"))
#         r=float(input("enter no:"))
#         t=float(input("enter no:"))
#         si=(p*r*t)/100
#         print(si)
#         i+=1  #this will increase thee itration numbe
    
    
    
    
    
    
#wap to print 1 to 10 using infinite loop        
# i=1       
# while True:
#     print(i)
#     if i==10:
#         break
#     i+=1


#wap to create all unique combinaation of 1 2 and 3

# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         k=1
#         while k<=3:
#             if i==j or j==k or k==i:
#                 k+=1
#                 continue
#             else:
#                 print(i,j,k)
#             k+=1
#         j+=1
#     i+=1



# i=1 
# while i <=3:
#     j=1
#     while j <=3:
#         k=1
#         while k <=3:
#             if (i!=j and j!=k and k!=i):
#                 print(i,j,k)
#             k+=1
#         j+=1
#     i+=1
    
    
    
# binary=int(input("enter binary no:"))
# decimal=0
# base=1
# while binary>0:
#     digit=binary%10
#     decimal=decimal+digit*base
#     base=base*2
#     binary=binary//10
# print(decimal)

# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         k=1
#         while k<=3:
#             if(i!=j and j!=k and k!=i):
#                 print(i,j,k)
#             k+=1
#         j+=1
#     i+=1
    


# i=1 
# while i <=3:
#     p=int(input("enter no:"))
#     r=int(input("enter no:"))
#     t=int(input("enter no:"))
#     si=(p*r*t)/100
#     print(si)
#     i+=1

# i=1
# while True:
#     print(i)
#     i+=1
#     if(i>10):
#         break


# i=1
# while i <=3:
#     j=1
#     while j<=3:
#         k=1
#         while k <=3:
#             if(i!=j and j!=k and k!=i):
#                 print(i,j,k)
#             k+=1
#         j+=1
#     i+=1



# binary=int(input("enter a no:"))
# base=1
# decimal=0
# while binary>0:
#     digit=binary%10
#     decimal=decimal+digit*base
#     base=base*2
#     binary//=10
# print(decimal)



# n=int(input("enter no:"))
# rev=0
# while n>0:
#     rev=rev*10+(n%10)
#     n=n//10
# print(rev)
# if(rev==n):
#     print("equal")
# else:
#     print("not equal")


# i=3
# while i!=0:
#     print("meow")
#     i-=1


i=0
while i <3:
    print("meow")
    i+=1