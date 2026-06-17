# let's check validation of email
# email=input("enter mail id:")
# username,domain=email.split("@")
# if username and"."in domain:
#     print("valid")
# else:
#     print("invalid")
# or
# if username and domain.endswith("gmail.com"):
#     print("valid")
# else:
#     print("invalid")






### we can do this using re library which checks any pattern
# import re
# email=input("enter mail id:")
# if re.search(".+@.+",email):
#     print("valid")
# else:
#     print("invalid")



import re
email=input("enter mail id:")
if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("valid")
else:
    print("invalid")