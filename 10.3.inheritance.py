# let's create inheritance by creating a superclass inheriting values to subclass

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("missing name")
        self.name=name
    ...

class Student(Wizard):
    def __init__(self, name,house):
        super().__init__(name)
        self.house=house
    def __str__(self):
        return (f"{self.name} is from {self.house}")
class Professor(Wizard):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject
    def __str__(self):
        return (f"{self.name} teaches {self.subject}")
wizard=Wizard("albus")
student=Student("harry","gryfindor")
professor=Professor("serbus","arts")

def main():
    print(student)
    print(professor)

if __name__=="__main__":
    main()