# name="ayush"   #strings are immutable it means we cannot change the value of string

# a=len(name)  # len() function gives length of string
# print(a)
# print(name.upper())  # upper() function converts string to uppercase
# print(name.lower())  # lower() function converts string to lowercase
# print(name.capitalize())  # capitalize() function capitalizes first letter of string
# print(name.count('h'))  # count() function counts number of occurrences of a substring in string
# print(name.replace('a', 'A'))  # replace() function replaces a substring with another substring
# print(name.find('h'))  # find() function returns the index of first occurrence of a substring in string
# print(name.isalpha())  # isalpha() function checks if all characters in string are alphabets
# print(name.isdigit())  # isdigit() function checks if all characters in string are digits
# print(name.split('h'))  # split() function splits string into a list of substrings based on a delimiter
# print(name.title())  # title() function converts first letter of each word to uppercase
# text = "  hello world  "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world"

# text = "Python is fun"
# print(text.find("fun")) # Output: 7
# print(text.replace("fun", "awesome")) # Output: "Python is awesome"


# text = "apple,banana,orange"
# fruits = text.split(",")
# print(fruits) # Output: ['apple', 'banana', 'orange']
# print(name.startswith('a'))  # startswith() function checks if string starts with a substring

# new_text = " ... ".join(fruits)
# print(new_text) # Output: "apple - banana - orange"


name="           ayush                   "
print (name.strip().upper())