
# now let's move on to class methods
''' 1 __init__ =  __init__ is a function that automatically runs when you
 create an object and gives that object its starting values.'''
# class Student:
#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
# def main():
#     student=get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()


# but what if user provided wrong input then we can raise error 
# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("missing name")
#         if not house:
#             raise ValueError("missing house")
#         self.name=name
#         self.house=house
# def main():
#     student=get_student()
#     print(f"{student.name} from {student.house}")
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()







# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("missing name")
#         if not house:
#             raise ValueError("missing house")
#         self.name=name
#         self.house=house
# def main():
#     student=get_student()
#     print(student)
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()


# here when we tried to print an object#### <__main__.Student object at 0x0000027EE7B97230> ##### this is the memory location output to solve this we use a method __str__ to control the output 

'''  __str__ = is used to get control over object and its output , instead of giving memory location it will give some output too

'''

# class Student:

#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("missing name")
#         if not house:
#             raise ValueError("missing house")
#         self.name=name
#         self.house=house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
# def main():
#     student=get_student()
#     print(student)
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()





## now we can create our own function aka methods 


# class Student:

#     def __init__(self,name,house,patronus):
#         if not name:
#             raise ValueError("missing name")
#         if not house:
#             raise ValueError("missing house")
#         self.name=name
#         self.house=house
#         self.patronus=patronus
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#     def charm(self):
#         match self.patronus:
#             case "stag":
#                 return "💕"
#             case "otter":
#                 return"❤️"
#             case "jack":
#                 return"🙌"
#             case _:
#                 return "👌"
# def main():
#     student=get_student()
#     print("patronoum expecto")
#     print(student.charm())
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     patronus=input("patronus:")
#     return Student(name,house,patronus)
# if __name__=="__main__":
#     main()






### what if til now anyone can rewrite data 
# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("missing name")
#         if not house:
#             raise ValueError("missing house")
#         self.name=name
#         self.house=house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
# def main():
#     student=get_student()
#     student.house="hoor"  
#     # it will overwrite output of house
#     print(student)
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()




### to solve this problem  we use decorators getter  and setters

# class Student:
#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     # getter 
#     @property
#     def house(self):
#         return self._house
    
#     # setter
#     @house.setter
#     def house(self,house):
#         if house not in ["mahupi","garhwa"]:
#             raise ValueError("invalid house")
#         self._house=house
# def main():
#     student=get_student()
#     #student.house="hoor"  # now after setting setter this line will not work
#     # it will overwrite output of house
#     print(student)
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()




### we can do this for name too
# class Student:
#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
    
    
#     #getter 
#     @property
#     def name(self):
#         return self._name
    
    
#     # setter
#     @name.setter
#     def name(self,name):
#         if not name:
#             raise ValueError("invalid name")
#         self._name=name
        
#     # getter 
#     @property
#     def house(self):
#         return self._house
    
#     # setter
#     @house.setter
#     def house(self,house):
#         if house not in ["mahupi","garhwa"]:
#             raise ValueError("invalid house")
#         self._house=house
# def main():
#     student=get_student()
#     #student.house="hoor"  # now after setting setter this line will not work
#     # it will overwrite output of house
#     print(student)
# def get_student():
#     name=input("name: ")
#     house=input("house: ")
#     return Student(name,house)
# if __name__=="__main__":
#     main()



### but but but someone can change it by changing name student._name =  "chaubey" or student._house="hoor"  
#because python provides ownership control it have control like normal for normal self.name, for protected self._name and for private self.__name












####### now lets see @classmethod


# let's create a class and instanciate an object

# import library for choices
# import random
# class Hat:
#     def __init__(self):
#         self.houses=["gryffindor","hufflepuff","ravenclaw","slytherin"]
#     def sort(self,name):
#         print(name, "is in ",random.choice(self.houses))
        
# hat=Hat()
# hat.sort("harry")



## till now we use __init__(self) as it works only for specific object of the class but for entire class we use class methods 

# import random
# class Hat:
#     houses=["gryffindor","hufflepuff","ravenclaw","slytherin"]
#     @classmethod
#     def sort(cls,name):
#         print(name, "is in ",random.choice(cls.houses))
        
# Hat.sort("harry")








## from our previous problem of class Student we had created a function to get student data outside the class . we can solve this by classmethod

# class Student:

#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#     @classmethod    
#     def get(cls):
#         name=input("name: ")
#         house=input("house: ")
#         return cls(name , house)
# def main():
#     student=Student.get()
#     print(student)

# if __name__=="__main__":
#     main()

