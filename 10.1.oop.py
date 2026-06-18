# def main ():
#     name=get_name()
#     house=get_house()
#     print(f"{name} is from {house}")
# def get_name():
#     return input("enter name:")
# def get_house():
#     return input("enter house:")
# if __name__=="__main__":
#     main()



# or we can do this in other way using concept of tuple


# def main ():
#     name,house=get_student()
#     print(f"{name} is from {house}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return (name,house)
# if __name__=="__main__":
#     main()



## or in another approach here


# def main ():
#     student=get_student()
#     print(f"{student[0]} is from {student[1]}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return (name,house)
# if __name__=="__main__":
#     main()


# here if we try to assign a value we will get typeerror means tuple doesn't allow this

# def main ():
#     student=get_student()
#     if student[0]=="pawan":
#         student[1]="garhwa"
#     print(f"{student[0]} is from {student[1]}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return (name,house)
# if __name__=="__main__":
#     main()

# here if i go this will give type error[TypeError: 'tuple' object does not support item assignment]
#in this context we can use a list as return value
# def main ():
#     student=get_student()
#     if student[0]=="pawan":
#         student[1]="garhwa"
#     print(f"{student[0]} is from {student[1]}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return [name,house]
# if __name__=="__main__":
#     main()





## now let's do it in a  better way
# def main ():
#     student=get_student()
#     print(f"{student['name']} is from {student['house']}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return {"name":name,"house":house}
# if __name__=="__main__":
#     main()


## here dictionary are mutable so we can assign values whatever we want unlike tuples
# def main ():
#     student=get_student()
#     if student['name']=="ayush":
#         student['house']="garhwa"
#     print(f"{student['name']} is from {student['house']}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     return {"name":name,"house":house}
# if __name__=="__main__":
#     main()









### now let's create a class 
# class Student:
#     ...
# def main ():
#     student=get_student()
#     print(f"{student.name} is from {student.house}")
# def get_student():
#     student=Student()
#     student.name=input("name:")
#     student.house=input("house:")
#     return student
# if __name__=="__main__":
#     main()


# or we can do this without creating an object
# class Student:
#     ...
# def main ():
#     student=get_student()
#     print(f"{student.name} is from {student.house}")
# def get_student():
#     name=input("name:")
#     house=input("house:")
#     student=Student(name,house)
#     return student
# if __name__=="__main__":
#     main()















# now let's move on to class methods

