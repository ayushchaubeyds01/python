# students={"ayush":"garhwa",
#           "anku":"daltongunj",
#           "ankit":"ghataua kalan"
#           }
# # print(students["ayush"])
# # print(students["anku"])
# # print(students["ankit"])      a simple manual method 


# for student in students:
#     print(student, students[student],sep=" , ")



# students =[
#     {"name":"ayush","house":"garhwa","patronous":"stag"}
#     {"name":"anku","house":"daltongunj","patronous":"otter"}
#     {"name":"ankit","house":"ghatauwa kalan","patronous":None}
# ]
       
# students = [
#     {"name": "ayush", "house": "garhwa", "patronous": "stag"},
#     {"name": "anku", "house": "daltongunj", "patronous": "otter"},
#     {"name": "ankit", "house": "ghatauwa kalan", "patronous": None}
# ]


# for student in students :
#     print(student["name"],student["house"],student["patronous"],sep=",")


# marks={"Ayush":56,"satyam":99}
# print(marks)
# print(marks["Ayush"])





#dictionarry methods
# print(marks.keys())
# print(marks.values())
# print(marks.pop("satyam"))
# print(marks.clear())




#dictionary comprehension
table={i:5*i for i in range(1,11)}
print(table)