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


## for restriction of @ before @ of domain to validate email and to be precise
# import re
# email=input("enter mail id:")
# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")





#now we can do this in better way by validating each character 
# import re
# email=input("enter mail id:")
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")


## or we can use regexes symbols like \w that contains all alphanumeric characters
# import re
# email=input("enter mail id:")
# if re.search(r"^\w+@\w+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")



##to be more precise for case senstivity we use flags that tells how regexws enginee behaves
# import re
# email=input("enter mail id:")
# if re.search(r"^\w+@\w+\.edu$",email,re.IGNORECASE):  ##re.IGNORECASE ignores the case senstivit
#     print("valid") 
# else:
#     print("invalid")






##  now let's just validate a name input from user
# import re
# name=input(("enter name:"))
# matches=re.search(r"^(.+), *(.+)$",name)
# if matches:
#     last,first=matches.groups()
#     name=f"{first} {last}"
# print(f"hello ,{name}")



# we can do this in a better way  using   walrus oprator :=
# import re
# name=input(("enter name:"))
# if matches :=re.search(r"^(.+), *(.+)$",name):
#     name=matches.groups(2)+" "+matches.group(1)
# print(f"hello ,{name}")










########33 now just let's take another example by extracting username from url of twitter

#for this we are using another function of regexes
#  re.sub(pattern , repl , string ,count=0 , flags=0)
# import re
# url=input("url:")
# username=re.sub("^(https?://)?(www\.)?twitter\.com/","",url)
# print(username)





#but what if user gives input unexpectedly wrong and there can be various corner cases then let's switch back to re.search with a conditional question 
# import re
# url=input("url:")
# if matches:=re.search("^(https?://)?(www\.)?twitter\.com/(.+)",url,re.IGNORECASE):
#     print(matches.groups(2))




# but we can use a non capturing version of regexes using walrus oprator
# import re
# url=input("url:")
# if matches:=re.search("^(https?://)?(?:www\.)?twitter\.com/(.+)",url,re.IGNORECASE):
#     print(matches.groups(2))



#our better and final version will be 
# import re
# url=input("url:")
# if matches:=re.search("^(https?://)?(?:www\.)?twitter(?:\.com)/([a-z0-9_]+)",url,re.IGNORECASE):
#     print(matches.groups(2))


