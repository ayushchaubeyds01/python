# name=input("enter name:")
# file=open("names.txt","w")   #  w to write
# file.write(name)
# file.close()


# name=input("enter name:")
# file=open("names.txt","a")   #   a to append
# file.write(name)
# file.close()


# # another way of writting it 
# name=input("enter name:")
# with open("names.txt","a")  as file: #   a to append
#     file.write (f"{name}\n")






# now to read these saved 

# with open("names.txt","r") as file:
#     lines=file.readlines()
# for line in lines:
#     print("hello,",line)

# we can do it in a better way



# with open("names.txt","r") as file:
#     for line in file:
#         print(line.rstrip())





# how is it if we just sort the names before printing

# names=[]

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names ):
#     print (name)





# we can sort it in descending order too (z-a)
# names=[]

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names ,reverse=True ):
#     print (name)






# now we can just create a csv file (comma separated values)file

# with open ("names.csv") as file:
#     for line in file :
#         row=line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")


# we can do this in another way

# with open ("names.csv") as file:
#     for line in file :
#         name,house=line.rstrip().split(",")
#         print(f"{name} is in {house}")






### now we can sort using a dictionary
# names=[]
# with open ("names.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         names.append(student)
# for student in names:
#     print(f"{student['name']} is in {student['house']}")



