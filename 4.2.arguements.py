def add(a,b):   #here a and b are parameters 
    return a+b
c=add(3,4)           #3 and 4 are the arguements
print(c) 


# def greet(name="guests"):
#     return f"hello:{name}"
# print(greet())



def greet(name):
    return f"hello:{name}"
print(greet("ayush"))
greet(name="ayush")


def student (name,age):
    return (f"name={name},age={age}")
print(student(name="ayush",age=20))
