def main ():
    student=get_student()
    if student[0]=="pawan":
        student[1]="garhwa"
    print(f"{student[0]} is from {student[1]}")
def get_student():
    name=input("name:")
    house=input("house:")
    return (name,house)
if __name__=="__main__":
    main()