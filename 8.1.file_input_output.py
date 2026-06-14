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



# to sort it
# names=[]
# with open ("names.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         names.append(student)
# def get_name(student):
#     return student ["name"]
# for student in sorted(names ,key=get_name):
#     print(f"{student['name']} is in {student['house']}")


# to reverse sort it
# names=[]
# with open ("names.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         names.append(student)
# def get_name(student):
#     return student ["name"]
# for student in sorted(names ,key=get_name,reverse=True):
#     print(f"{student['name']} is in {student['house']}")






# we can do it using a lambda function
# names=[]
# with open ("names.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         names.append(student)

# for student in sorted(names ,key=lambda student:student["name"]):
#     print(f"{student['name']} is in {student['house']}")







# we can do all this readings of csv files using a module
# import csv
# students=[]
# with open ("names.csv") as file:
#     reader=csv.reader(file)
#     for name ,home in reader:
#         students.append({"name":name ,"home":home})
# for student in sorted(students ,key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")



# instead of it we can use a dictionary reader 
# import csv
# students=[]
# with open ("names.csv") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"],"home":row["home"]})
# for student in sorted(students ,key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# or it can be like this because a dictionary already exists in the name of row

# import csv
# students=[]
# with open ("names.csv") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         students.append(row)
# for student in sorted(students ,key=lambda student:student["name"]):
#     print(f"{student['name']} is from {student['home']}")



# now we can write a csv file

# import csv
# name=input("enter:")
# home=input("enter:")
# with open ("names.csv","a") as file:
#     writer=csv.writer(file)
#     writer.writerow([name,home])


# now here we can also use dictonary writter
# import csv
# name=input("enter:")
# home=input("enter:")
# with open ("names.csv","a") as file:
#     writer=csv.DictWriter(file,fieldnames=["name","home"])
#     writer.writerow({"name":name,"home":home})





# not just we can open read or write text formats files we can create gif files , images ,videos etc
# import sys 
# from PIL import Image
# images=[]
# for arg in sys.argv[1:]:
#     image=Image.open(arg)
#     images.append(image)
    
# images[0].save(
#     "costumes.gif",save_all=True ,append_images=[images[1]] ,duration=200 ,loop=0
# )